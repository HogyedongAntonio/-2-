import random

# 가위바위보 옵션
options = ["가위", "바위", "보"]

def get_user_choice():
    """사용자로부터 가위, 바위, 보 중 하나를 입력받습니다."""
    while True:
        user_choice = input("가위, 바위, 보 중 하나를 선택하세요: ")
        if user_choice in options:
            return user_choice
        else:
            print("잘못된 입력입니다. 가위, 바위, 보 중 하나를 입력하세요.")

def get_computer_choice():
    """컴퓨터의 선택을 랜덤으로 결정합니다."""
    return random.choice(options)

def determine_winner(user_choice, computer_choice):
    """사용자와 컴퓨터의 선택을 비교하여 승패를 결정합니다."""
    if user_choice == computer_choice:
        return "비겼습니다."
    elif (user_choice == "가위" and computer_choice == "보") or \
         (user_choice == "바위" and computer_choice == "가위") or \
         (user_choice == "보" and computer_choice == "바위"):
        return "이겼습니다!"
    else:
        return "졌습니다ㅠㅠ"

def play_game():
    """가위바위보 게임을 실행합니다."""
    while True:
        print("가위바위보 게임에 오신 것을 환영합니다!")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"컴퓨터: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        play_again = input("게임을 계속하시겠습니까? (Y/N): ").strip().upper()
        if play_again != 'Y':
            print("가위바위보 게임을 종료합니다.")
            break

if __name__ == "__main__":
    play_game()
