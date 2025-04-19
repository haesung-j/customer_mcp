# Customer MCP

LangChain과 MCP를 활용한 예제 프로젝트입니다.

## 프로젝트 설정

### 1. uv 설치

```bash
# Windows (PowerShell)
iwr https://astral.sh/uv/install.ps1 -useb | iex

# Linux/macOS
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. 프로젝트 설정

```bash
# 프로젝트 클론
git clone [프로젝트 URL]
cd customer-mcp

# 가상환경 생성 및 의존성 설치
uv venv
uv pip install -r requirements.txt
```

### 3. 환경 변수 설정

`.env` 파일을 생성하고 다음 환경 변수를 설정합니다:

```
OPENAI_API_KEY=your_api_key_here
```

## 프로젝트 구조

- `mcp_sample/`: MCP 샘플 코드
- `vector_store/`: 벡터 저장소 관련 파일
- `ai_agent.ipynb`: AI 에이전트 실험 노트북
