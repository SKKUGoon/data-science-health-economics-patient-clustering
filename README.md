# 병원 물류, 호텔 물류, 그 모든것의 물류

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white">

새로운 데이터를 맞이하는 차원에서

새롭게 만들어냈습니다. 

## 필요한 시스템

* Docker: https://docs.docker.com/engine/install/
  * 윈도우 시스템이라면, WSL(Window Subsystem for Linux)를 실행시켜서 만드는 것이 더 빠를 수도 있습니다.
  * MacOS면 따라하시면 됩니다.
  * Docker Hub를 까는것이 편합니다. 

## How to start

1. `docker compose up -d` 라고 입력한다. 혹은 `docker-compose up -d`
  - Qdrant 벡터 데이터베이스가 시작됨
2. `data/20250512` 폴더를 만들고, 그 안에 하나이비인후과가 준 최신 데이터를 이름을 바꾸지 않고, xlsx 파일만 전부다 삽입.
3. 프로젝트 루트에 `.env` 파일 생성

    ```BASH
    OPENAI_API_KEY=sk-proj-...
    ```

4. `001-....ipynb` 파일부터 보면서 천천히 따라합시다.