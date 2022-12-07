install: # установка пакета (poetry создаст виртуальное окружение и установит пакет в него)
	poetry install

brain-games:
	poetry run brain-games

build: # собрать пакет
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl


