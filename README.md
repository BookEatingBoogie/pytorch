# pytorch 설치하는 방법

처음에 이렇게 프로젝트를 생성하셔야 합니다. 
(clone 할거면 상관없긴 하겟네요..머쓱)

<img width="816" alt="스크린샷 2025-03-13 오후 10 30 17" src="https://github.com/user-attachments/assets/efc171af-db5d-4932-b43b-ca3cf1a09f18" />

아마 클론해도 pytorch가 안 깔려있을거임
인텔리제이 터미널에 다음과 같은 명령어 입력

pip install torch torchvision torchaudio

설치가 되면 자동으로 업데이트 되고 오류가 없어짐!

실행이 잘 되면 

<img width="296" alt="스크린샷 2025-03-13 오후 10 33 02" src="https://github.com/user-attachments/assets/d942d14f-84a0-4a0e-8590-2fac371705ba" />

이런 결과가 나옵니다~ 
bb


## pytorch 다시 활성화하는 방법

인텔리제이를 끄면 자동으로 비활성화 되고,
다시 활성화하려면

cd /Users/leeseoyoung/Desktop/Caps/workspace/pytorch_project  # 프로젝트 폴더로 이동

source venv/bin/activate  # 가상환경 다시 활성화

이렇게 하면 됩니다 (_ _)

+) 근데 제가 인텔리제이 다시 켜서 실행해보니까 자동으로 활성화되는 것 같아요 위에 작성한 건 비활성화 하고 다시 활성화할 때라고 생각하시면 될 듯 합니다

