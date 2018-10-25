# Writable

This is a harder machine, using a much more obscure technique.

## Solution

### User

* Scan box
* See a list of processes of the current user
* Use redis to overwrite /home/tom/.ssh/authorized_hosts
* Login
* Get flag

### Root

* Check running processes.
* See a web server running on localhost
