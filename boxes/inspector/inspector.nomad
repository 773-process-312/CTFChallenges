job "inspector" {
    type = "service"
    datacenters = ["do_ams3"]
    group "main" {
        count = 1
        task "inspector" {
            driver = "docker"
            config {
                image = "bhorn/boot2root-inspector"
                ipv4_address = "10.10.2.2" 
                network_mode = "ctfnet"    
            }
            resources {
                memory = 500
                cpu = 400
            }
        }
    }
}
