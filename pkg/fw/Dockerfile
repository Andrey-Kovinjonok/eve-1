FROM alpine:edge as build

WORKDIR /
RUN apk add --no-cache \
    wireless-regdb \
    linux-firmware-bnx2x \
    linux-firmware-other \
    linux-firmware-ath10k \
    linux-firmware-mrvl \
    linux-firmware-rtlwifi \
    linux-firmware-rsi \
    linux-firmware-nvidia \
    linux-firmware-other

FROM scratch
ENTRYPOINT []
WORKDIR /
COPY --from=build /lib/firmware/regulatory* /lib/firmware/
COPY --from=build /lib/firmware/bnx2x/* /lib/firmware/bnx2x/
COPY --from=build /lib/firmware/mrvl/*.bin /lib/firmware/mrvl/
COPY --from=build /lib/firmware/rt2870.bin /lib/firmware/rt2870.bin
COPY --from=build /lib/firmware/rtlwifi/*.bin /lib/firmware/rtlwifi/
COPY --from=build /lib/firmware/iwlwifi-8265* /lib/firmware/
COPY --from=build /lib/firmware/iwlwifi-7260* /lib/firmware/
COPY --from=build /lib/firmware/iwlwifi-9260* /lib/firmware/
# NVidia Jetson
COPY --from=build /lib/firmware/nvidia/tegra210 /lib/firmware/nvidia/tegra210
# Dell Edge Gateway 300x firmware
COPY --from=build /lib/firmware/rsi* /lib/firmware/rsi/
# FIXME: this is a binary block firmware for Raspberry Pi4, waiting for linux-firmware-rpi4 package
COPY rpi /lib/firmware/
# FIXME: we're currently using ath10k firmware supplied
# by Advantech. This is getting upstreamed and when it
# does we should switch back to linux-firmware-ath10k from Alpine
# COPY --from=build /lib/firmware/ath10k /lib/firmware/ath10k
COPY ath10k /lib/firmware/ath10k
# FIXME: this is binary block firmware for HiKey
COPY ti-connectivity /lib/firmware/ti-connectivity
