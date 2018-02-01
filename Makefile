# project
PROJECT = $(shell pwd)
SOURCE  = $(PROJECT)/hmd
BUILD   = $(PROJECT)/build
OUTPUT  = $(PROJECT)/build/hmd

all:
	mkdir -pv $(BUILD)
	cd $(SOURCE) && \
	   zip -rv $(OUTPUT).zip * && \
	   echo "#!/usr/bin/python" > $(OUTPUT) && \
	   cat $(OUTPUT).zip >> $(OUTPUT)
	rm -fv $(OUTPUT).zip
	chmod u+x -v $(OUTPUT)

test:
	python $(SOURCE) -t

clean:
	rm -rfv $(BUILD)
	find $(SOURCE) \
	     -type f \
	     -iname "*.py[oc]" \
	     -exec rm -fv "{}" \;
