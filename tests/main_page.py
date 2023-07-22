import allure


@allure.title('Покупка товара')
def test_buy_item():
    with allure.step('Покупаем товар'):
        assert 1 == 2


@allure.title('Очистка корзины')
def test_clear_basket():
    with allure.step('Очищаем корзину'):
        assert 1 == 1


@allure.title('Удаляем товар из корзины')
def test_remove_item():
    with allure.step('Удаляем товар из корзины'):
        assert 1 == 2


@allure.title('Добавляем товар в корзину')
def test_add_item():
    with allure.step('Добавляем товар в корзину'):
        assert 1 == 1
