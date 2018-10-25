# Clippy

Clippy is designed to be an easy machine.

Basically, this is a simple direct reference bug for user and script the user
can run via sudo.

## Overview of Process

### User

### Root

* Run `sudo -l` and see what you can do.
* See that they can run one command without a password.
* It lets them run find. They pass an arg to find and get a bash shell.
