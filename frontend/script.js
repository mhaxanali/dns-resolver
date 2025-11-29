const resultsPlaceholder = document.getElementById("results-placeholder")
const input = document.getElementById("domain-input")
const btn = document.getElementById("resolve-btn")

btn.addEventListener("click", () => {
    const domain = input.value  // Read value when clicked
    resolve(domain)
})

function resolve(domain) {
    const container = document.getElementById("results-container")
    
    fetch(`http://localhost:8080/lookup?domain=${domain}`)
        .then(res => res.json())
        .then(data => {
            container.innerHTML = `<p style="color: #00e0ff; font-size: 1.5rem;">IP: ${data.ip}</p>`
        })
}