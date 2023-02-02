GIT=git

ADD=add
COMMIT=commit
PUSH=push

ORIGIN=origin
BRANCH=$(shell git branch | grep -E "^\* .+" -o | grep -E "[^* ]+" -o)

commit:* .gitignore
	-$(GIT) $(ADD) $^
	$(GIT) $(COMMIT)

push:commit
	$(GIT) $(PUSH) $(ORIGIN) $(BRANCH)
