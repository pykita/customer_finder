.PHONY: tests
tests:
	python3 -m unittest tests/test_*

.PHONY: run
run:
	python3 -m cli --input-file customers.txt --output-file output.txt --radius 100
