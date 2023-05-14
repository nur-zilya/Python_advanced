import getpass
import hashlib
import logging

logger = logging.getLogger("password_checker")


def input_and_check_password():
    logger.debug("Начало функции")
    password: str = getpass.getpass()

    count_numb = int(input("Введите кол-во попыток от 2 до 10: "))
    if count_numb < 2 or count_numb > 10:
        logger.error("Кол-во должно быть от 2 до 10")
    if not password:
        logger.warning("Вы ввели пустой пароль")
        return False

    if len(password) < 8:
        logger.warning("Пароль должен содержать не менее 8 символов")
        return False

    if not any(char.isdigit() for char in password):
        logger.warning("Пароль должен содержать хотя бы одну цифру")
        return False

    special_chars = "!@#$%^&*()-+=_"
    if not any(char in special_chars for char in password):
        logger.warning(f"Пароль должен содержать хотя бы один символ из списка: {special_chars}")
        return False

    if password.isalpha() or password.isdigit():
        logger.warning("Пароль должен содержать буквы и цифры")
        return False

    try:
        hasher = hashlib.md5()
        logger.debug(f"Мы создали объект hasher {hasher!r}")
        hasher.update(password.encode("utf-8"))
        logger.debug("Кодировка пароля в 'utf-8'")

        if hasher.hexdigest() == "098f6bcd4621d37cade4e892627b4f6":
            return True

    except ValueError as ex:
        logger.exception("Вы ввели некорректный символ", exc_info=ex)

    return False


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    logger.info("Вы пытались авторизироваться")
    count_numb = int(input("Введите кол-во попыток от 1 до 10"))
    if count_numb < 1 or count_numb > 10:
        logger.error("Кол-во должно быть от 1 до 10")
    logger.info(f"У вас есть {count_numb} попыток")

    while count_numb > 0:
        if input_and_check_password():
            exit(0)
        count_numb -= 1

    logger.error("Пользователь ввел неправильный пароль трижды")
    exit(1)