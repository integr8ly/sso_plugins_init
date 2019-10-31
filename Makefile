ORG=integreatly
PROJECT=sso_plugins_init
REG=quay.io
TAG=2.0.0
PKG=github.com/integr8ly/sso_plugins_init
ENGINE?=docker

.PHONY: image/build
image/build:
	${ENGINE} build -t ${REG}/${ORG}/${PROJECT}:${TAG} .

.PHONY: image/push
image/push:
	${ENGINE} push ${REG}/${ORG}/${PROJECT}:${TAG}
