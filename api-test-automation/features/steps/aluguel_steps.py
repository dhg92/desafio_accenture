import random
import json
from behave import given, when, then
from support.api.end_points import EndPoints
from support.models.user import User
from support.assertions import assert_book_count, assert_user_has_isbns



@given('que um novo usuário é criado com o username "{username}" e a senha "{password}"')
def step_impl(context, username, password):
    context.api = EndPoints()
    context.username = username
    context.password = password
    response = context.api.create_user(username, password)
    assert response.status_code == 201
    response_data = response.json()
    context.user_id = response_data["userID"]

@given("o usuário realiza login com sucesso")
def step_impl(context):
    token_response = context.api.generate_token(context.username, context.password)
    assert token_response.status_code == 200
    response_data = token_response.json()
    assert "token" in response_data
    context.token = response_data["token"]
    auth_response = context.api.authorize_user(context.username, context.password)
    assert auth_response.status_code == 200

@when("o usuário acessa a listagem de livros disponíveis")
def step_impl(context):
    response = context.api.get_books()
    assert response.status_code == 200
    context.books = response.json()["books"]
    books_summary = [{"isbn": b.get("isbn"), "title": b.get("title")} for b in context.books]

    print("Livros disponíveis:")
    print(json.dumps(books_summary, indent=2))


@when("seleciona dois livros para alugar")
def step_impl(context):
    selected_books = random.sample(context.books, 2)
    context.selected_isbns = [book["isbn"] for book in selected_books]
    response = context.api.rent_books(context.user_id, context.selected_isbns, context.token)
    assert response.status_code == 201, f"Falha ao alugar livros: {response.text}"

    context.selected_books = selected_books

    print("Livros selecionados:")
    print(json.dumps([{"isbn": book["isbn"], "title": book["title"]} for book in selected_books],indent=2))

@then("o sistema deve mostrar os detalhes do usuário")
def step_impl(context):
    response = context.api.get_user_details(context.user_id, context.token)
    assert response.status_code == 200
    user_info = response.json()
    assert user_info["userId"] == context.user_id 

@then("os dois livros alugados devem estar associados a esse usuário")
def step_impl(context):
    user_response = context.api.get_user_details(context.user_id, context.token)
    assert user_response.status_code == 200, f"Falha ao buscar detalhes do usuário: {user_response.text}"
    json_data = user_response.json()
    context.user = User(json_data)
    
    print("Detalhes do usuário retornados pela API:")
    print(json.dumps(json_data, indent=2))

    assert_book_count(context.user, 2)
    assert_user_has_isbns(context.user, context.selected_isbns)
    