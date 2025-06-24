def before_all(context):
    context.base_url = "https://demoqa.com"
    context.headers = {}

def before_scenario(context, scenario):
    print(f"\nRodando cenário: {scenario.name}")

def after_scenario(context, scenario):
    if scenario.status == "failed":
        print(f"Cenário falhou: {scenario.name}")
    if hasattr(context, "user_id") and hasattr(context, "token"):
        response = context.api.delete_user(context.user_id, context.token)
        print(f"Usuário {context.user_id} deletado com status {response.status_code}")