package api

import (
	"encoding/json"
	"fmt"
	"net"
	"net/http"

	"github.com/mhaxanali/dns-resolver/backend/log"
)

type Response struct {
	IP string `json:"ip"`
}

func handler(w http.ResponseWriter, r *http.Request) {

	var ip string

	domain := r.URL.Query().Get("domain")

	res, err := http.Get("http://localhost:5050/lookup?domain=" + domain)
	if err != nil {
		log.Warning(fmt.Sprintf("Error fetching response: %v", err))
		return
	}
	defer res.Body.Close()

	var data map[string]interface{}
	json.NewDecoder(res.Body).Decode(&data)

	if data["ip"] == nil {
		ips, err := net.LookupHost(domain)

		ip = ips[0]

		if err != nil {
			log.Warning(fmt.Sprintf("Error looking for host for %s: %v", domain, err))
			return
		}

		resp, err := http.Get("http://localhost:5050/store?domain=" + domain + "&ip=" + ip)

		if err != nil {
			log.Warning(fmt.Sprintf("Error sending store request: %v", err))
		}
		defer resp.Body.Close()

	} else {
		ip = data["ip"].(string)
	}

	response := Response{
		IP: ip,
	}

	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusOK)

	json.NewEncoder(w).Encode(response)
}

func main() {

	http.HandleFunc("/lookup", func(w http.ResponseWriter, r *http.Request) {
		handler(w, r)
	})

	log.Info("Service started.")
	if err := http.ListenAndServe(":8080", nil); err != nil {
		log.Fatal("Failed to start service.")
	}
}
