DESTDIR=/

.PHONY: install remove

install:
	install -pD acti-recorder.conf $(DESTDIR)/etc/acti-recorder.conf
	install -pD acti-recorder $(DESTDIR)/usr/bin/acti-recorder
remove:
	rm -f $(DESTDIR)/etc/acti-recorder.conf $(DESTDIR)/usr/bin/acti-recorder

