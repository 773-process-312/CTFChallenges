job "writable" {
    type = "service"
    datacenters = ["do_ams3"]
    group "main" {
        count = 1
        task "writable" {
            driver = "docker"
            config {
                image = "bhorn/boot2root-writable"
                ipv4_address = "10.10.2.6" 
                network_mode = "ctfnet"    
            }
            resources {
                memory = 500
                cpu = 500
            }
        }
    }
}
