PWD    = $(shell pwd)

SOURCE = $(PWD)/hmdc
OUTPUT = $(PWD)/build/hmdc

all:
	mkdir -pv build
	cd $(SOURCE) && \
	   zip -rv $(OUTPUT).zip * && \
	   echo "#!/usr/bin/python" > $(OUTPUT) && \
	   cat $(OUTPUT).zip >> $(OUTPUT)
	rm -fv $(OUTPUT).zip
	chmod u+x -v $(OUTPUT)

test:
	python $(SOURCE) -t

clean:
	rm -rfv ./build
	find $(SOURCE) \
	     -type f \
	     -iname "*.py[oc]" \
	     -exec rm -fv "{}" \;
