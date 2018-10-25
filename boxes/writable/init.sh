#!/bin/sh
service ssh start
su tom -c "glances -w --port 8000" & \
    python /opt/pyexec.py & \
    su tom -c "redis-server --bind 0.0.0.0 --requirepass redis_is_really_secure"
