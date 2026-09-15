# BMAD в этом репозитории

## Что установлено

Официальный [BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD),
29 repo-scoped skills для Codex в `.agents/skills/`, runtime `_bmad/`.
Версия манифестов: **6.13.0-next**, upstream commit:
`94b6727b00c8316557828c8a8ff2a48ff60d60cc`.
Это снимок текущей ветки upstream с prerelease-маркером, а не заявление о стабильном релизе.
Снимок зафиксирован вместе с контрольными суммами в `bmad.lock.json`.

Файлы установлены официальным Skills CLI из checkout указанного commit с `--agent codex --copy`.
Runtime создан официальным `bmad/scripts/setup.py`. Копии обычные, без зависимостей
от абсолютного пути компьютера автора. Лицензия upstream сохранена в `third_party/BMAD-LICENSE`.
После clone повторный install не требуется. Нужна доступная команда `uv`.

## Как пользоваться

Откройте чат Codex в корне проекта и попросите использовать skill по имени.
[Codex читает skills из .agents/skills](https://learn.chatgpt.com/docs/build-skills).
Если они не появились, начните новый чат/перезапустите приложение. В CLI можно использовать `$bmad`.

| Ситуация | Skill |
|---|---|
| Неясно, с чего начать | `bmad` |
| Одна понятная задача | `bmad-build` |
| Несколько связанных задач | `bmad-spec`, затем `bmad-build` для каждой истории |
| Дополнительная проверка изменения | `bmad-code-review` |
| Нужен разговор о требованиях | `bmad-agent-pm` |
| Нужен разговор об архитектуре | `bmad-agent-architect` |

Для большого объёма доступны brief/PRD/architecture/epics/sprint skills;
их необходимость определяйте через `bmad`, а не запускайте весь набор автоматически.
Эти маршруты описаны в [официальном руководстве установленной версии](../.agents/skills/bmad/references/help.md).

## Общие документы и персональные настройки

`_bmad/config.toml` — командная конфигурация; `_bmad-output/` — документы работы.
Командные изменения этих файлов входят в PR. Личные `*.user.toml` исключены из Git.
Русский язык работы задан в AGENTS.md; содержимое официальных skills сохранено без перевода.
Новые документы называйте с номером задачи, когда workflow позволяет выбрать имя.
При фиксированном имени назначайте одного редактора; связывайте файл с Issue.

GitHub Project остаётся основной доской команды. Sprint-файлы BMAD — детали планирования;
после работы отражайте актуальный статус задачи в GitHub, не считайте доски автоматически связанными.

## Проверка и восстановление runtime

Из корня репозитория:

```bash
uv run python scripts/check_workspace.py
uv run --no-cache .agents/skills/bmad/scripts/setup.py --project-root . --skill .agents/skills/bmad --doctor --list-config-questions
uv run --no-cache .agents/skills/bmad/scripts/setup.py --project-root . --skill .agents/skills/bmad --doctor
```

Если первый doctor вернёт вопросы, попросите skill `bmad` завершить doctor с вашими ответами.
Не заменяйте файлы runtime вручную. Ошибку «uv not found» исправляйте установкой uv
и перезапуском терминала/Codex. Первый запуск scripts может требовать интернет для зависимостей uv.

## Обновление версии — отдельный PR

Один ответственный выбирает новый upstream commit и читает изменения.
Сначала сохраните все текущие изменения. В отдельном checkout BMAD выполните checkout
выбранного commit, затем в корне этого проекта:

```bash
npx --yes skills add /path/to/BMAD-METHOD --agent codex --skill '*' --copy --yes
```

Попросите `bmad` выполнить doctor; прочитайте отчёт и проверьте сохранность командных настроек.
Обновите provenance и хеши `bmad.lock.json`, лицензию при необходимости и эту страницу.
Skills CLI при установке из локальной папки создаёт `skills-lock.json` с путём компьютера:
не коммитьте его, здесь источником фиксации служат Git и `bmad.lock.json`.
Запустите все проверки и отдайте PR на ревью. Не обновляйте upstream автоматически у каждого участника.
