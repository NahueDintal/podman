mkdir -p ~/.config/containers/

nano ~/.config/containers/registries.conf

unqualified-search-registries = ["docker.io", "quay.io", "registry.fedoraproject.org"]

[[registry]]
location = "docker.io"
