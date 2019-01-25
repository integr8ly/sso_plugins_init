# RHSSO Plugins Init Container

This image contains a list of RHSSO (Keycloak) plugins that can be installed by the [Keycloak Operator](https://github.com/integr8ly/keycloak-operator). It should be used as an init container in the same Pod that runs Keycloak. The Python script reads the list of plugins from an environment variable (`SSO_PLUGINS`) and copies them, provided they are bundled with the image, to `/opt/plugins`. This is expected to be mounted to the same volume as the Keycloak providers directory.

## Building

To build and push the image run:

```sh
$ make image/build
$ make image/push
```
