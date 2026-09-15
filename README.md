# Municipal Economic Network

Общее рабочее пространство команды хакатона по кластеризации российских муниципалитетов
на динамических атрибутированных сетях.

**Здесь настроена совместная разработка: BMAD, структура кода, документация, задачи и проверки.**
Научная методология, алгоритмы и результаты будут определяться командой в ходе работы.

## С чего начать участнику

1. Открыть публичный репозиторий; участникам с правом записи принять приглашение владельца.
2. Клонировать проект и открыть его папку в Codex.
3. Прочитать [инструкцию команды](docs/TEAM_GUIDE.md).
4. Выбрать Issue, создать свою ветку и работать в ней.
5. Передать изменения через Pull Request с проверками и ревью коллеги.

```bash
git clone https://github.com/ZakBu/municipal-economic-network.git
cd municipal-economic-network
python3 -m pip install uv
uv sync --locked
uv run python scripts/check_workspace.py
```

Нужен Python 3.11+; стандарт команды — 3.12. `uv sync` создаёт `.venv` и ставит
зависимости из `uv.lock`. Если `uv` не найден, перезапустите терминал после установки.
Для запуска BMAD из Codex команда `uv` должна быть доступна в PATH приложения.

## BMAD уже подключён

В репозитории сохранены 29 официальных skills и готовый runtime.
В новом чате Codex, открытом в папке проекта, напишите:

```text
Используй skill bmad. Прочитай AGENTS.md и docs/PROJECT.md.
Помоги выбрать следующий шаг для моей задачи. Отвечай по-русски.
```

Для понятной небольшой задачи:

```text
Используй skill bmad-build. Выполни задачу из Issue <номер>.
Работай в моей ветке, проверь результат и подготовь описание PR.
```

Название skill можно выбрать через интерфейс skills; в Codex CLI также используется `$bmad`.
Если skill не появился, откройте новый чат или перезапустите Codex.
Подробнее: [BMAD_GUIDE](docs/BMAD_GUIDE.md).

Для подключения нового Codex или другого AI-агента используйте готовый промпт и проверку
прав из [AI_AGENT_ONBOARDING](docs/AI_AGENT_ONBOARDING.md). Он связывает документы,
GitHub Issues, [Kanban](https://github.com/users/ZakBu/projects/1), ветки и Pull Requests
в один рабочий цикл.

## Где что хранить

| Что | Где |
|---|---|
| Задачи, ответственные, обсуждение выполнения | [GitHub Issues](https://github.com/ZakBu/municipal-economic-network/issues) |
| Статусы задач | [GitHub Project #1](https://github.com/users/ZakBu/projects/1); [правила Kanban](docs/PROJECT_MANAGEMENT.md) |
| Идеи и вопросы | [docs/ideas/inbox.md](docs/ideas/inbox.md) |
| Требования и планы BMAD | `_bmad-output/planning-artifacts/` |
| Рабочие спецификации и истории BMAD | `_bmad-output/implementation-artifacts/` |
| Принятые решения | `docs/decisions/` |
| Код и тесты | `src/municipal_network/`, `tests/` |
| Конфигурации будущих экспериментов | `config/` |
| Описание источников и доступов | [data/README.md](data/README.md) |
| Локальные данные | `data/raw/`, `data/interim/`, `data/processed/` — вне Git |
| Отчёты и презентация | `reports/` |

## Проверки перед PR

```bash
uv run python scripts/check_workspace.py
uv run pytest
uv run ruff check .
uv run ruff format --check .
```

CI выполняет эти проверки на Python 3.11 и 3.12. Стартовые тесты проверяют установку
пакета и конфигурацию; по мере реализации добавляйте предметные тесты.
Сейчас проект не содержит вычислительного pipeline или готовых результатов исследования.

[Подключение AI-агента](docs/AI_AGENT_ONBOARDING.md) · [Правила вкладов](CONTRIBUTING.md) · [Контекст проекта](docs/PROJECT.md) ·
[Карта разделов](RESEARCH_MAP.md) · [Правила Codex](AGENTS.md)
