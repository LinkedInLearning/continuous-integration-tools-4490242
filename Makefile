dirs:
	@find . -type d -name 0\* -not -path '*/\.*' | sort

links:
	@for dir in $$(find . -type d -name ch\* | sort); do \
        cd "$$dir" && \
        for i in $$(find . ! -path ./README.md -type f -name README.md | sort); do \
            echo "- [$$(head -1 "$$i" | sed -e 's/# //')]($$i)"; \
        done; \
        cd - >/dev/null; \
    done

next:
	@for dir in $$(find . -type d -name ch\* | sort); do \
        cd "$$dir" && \
        for i in $$(find . ! -path ./README.md -type f -name README.md | sort); do \
            echo "[Next: $$(head -1 "$$i" | sed -e 's/# //')](.$$i)"; \
        done; \
        cd - >/dev/null; \
    done

edit:
	@vim $$(find . -type f -name README.md | sort)

spell:
	-find . -type f -name "*.md" -exec aspell check {} \;

clean:
	-find . -type f -name \*.bak -exec rm {} \; -print

