ORG=integreatly
PROJECT=sso_plugins_init
REG=quay.io
TAG=3.0.0
PKG=github.com/integr8ly/sso_plugins_init

.PHONY: image/build
image/build:
	docker build -t ${REG}/${ORG}/${PROJECT}:${TAG} .

.PHONY: image/push
image/push:
	docker push ${REG}/${ORG}/${PROJECT}:${TAG}
