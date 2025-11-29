package log

import (
	"fmt"
	"time"
)

func Warning(t string) {
	timestamp := time.Now().Format("2006-01-02 15:04:05")
	fmt.Println(timestamp + " | " + "[WARNING]" + " | " + "backend/api/api.go" + " | " + t)
}

func Info(t string) {
	timestamp := time.Now().Format("2006-01-02 15:04:05")
	fmt.Println(timestamp + " | " + "[INFO]" + " | " + "backend/api/api.go" + " | " + t)
}

func Fatal(t string) {
	timestamp := time.Now().Format("2006-01-02 15:04:05")
	fmt.Println(timestamp + " | " + "[FATAL]" + " | " + "backend/api/api.go" + " | " + t)
}
