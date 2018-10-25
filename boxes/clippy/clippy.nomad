job "clippy" {
    type = "service"
    datacenters = ["do_ams3"]
    group "main" {
        count = 1
        task "clippy" {
            driver = "docker"
            config {
                image = "bhorn/boot2root-clippy"
                ipv4_address = "10.10.2.3" 
                network_mode = "ctfnet"    
            }
            resources {
                memory = 500
                cpu = 400
            }
        }
    }
}
