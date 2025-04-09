#!/bin/bash
# Файл: capytol_bruteforce.sh
#
# Скрипт для автоматизации подбора строк, отправляемых в устройство /dev/capytol.
# Для каждого кандидата:
#   - Записывается строка в устройство.
#   - Считывается ровно столько байт, сколько символов в кандидате.
#   - Проводится сравнение: если считанная строка совпадает с кандидатом,
#     выводится уведомление о совпадении.
#
# Использование:
#   chmod +x capytol_bruteforce.sh
#   ./capytol_bruteforce.sh

device="/dev/capytol"

# Список кандидатов для тестирования. Подберите варианты по результатам предыдущих экспериментов.
candidates=(
  "SPbCTF{capy"
  "SPbCTF{get_flag"
  "SPbCTF{Kapibarovsk"
  "SPbCTF{capi"
  "SPbCTF{cap"
)

# Функция отправки кандидата и считывания результата
test_candidate() {
  local candidate="$1"
  local len=${#candidate}

  # Отправляем кандидата в устройство
  echo -ne "$candidate" > "$device"
  # Небольшая задержка (можно корректировать по необходимости)
  sleep 0.2

  # Считываем ровно столько байт, сколько символов в кандидате
  output=$(dd if="$device" bs=1 count=$len 2>/dev/null)

  # Сравниваем отправленную строку с полученной
  if [ "$output" == "$candidate" ]; then
    echo "[MATCH] Candidate: '$candidate' || Output: '$output'"
  else
    echo "[NO MATCH] Candidate: '$candidate' || Output: '$output'"
  fi
}

echo "=== Старт автоматизированного подбора через $device ==="
for candidate in "${candidates[@]}"; do
  test_candidate "$candidate"
done
