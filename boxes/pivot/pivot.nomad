job "pivot" {
    type = "service"
    datacenters = ["do_ams3"]
    group "main" {
        count = 1
        task "pivot" {
            driver = "docker"
            config {
                image = "bhorn/boot2root-pivot"
                ipv4_address = "10.10.2.1" 
                network_mode = "ctfnet"    
            }
            resources {
                memory = 100
                cpu = 100
            }
        }
    }
}
