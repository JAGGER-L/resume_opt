# resume_opt
resume_opt is a smart AI assistant that helps you create the perfect resume in seconds. Just input the job description and your current resume — it will instantly generate a customized, highly targeted resume tailored for that role.

# Key Features

- **Multi-Version Resume Generation**  
  Generate **3 tailored resumes** with different emphases in one click.

- **Interview Question Predictor**  
  Automatically generate the **10-15 most likely interview questions** based on the job description and your optimized resume, along with suggested thinking frameworks and key points for answering them.

- **Multiple Export Formats**  
  Export your resumes and supporting documents in various formats, including **PDF, Markdown, Word**.

- **Support multiple languages**
  As of now, **zh** and **en** are supported.

# Backend MVP

The first backend version is a local/personal FastAPI service. It supports pasted text input only and returns the optimized result synchronously.

## Run locally

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -e .
copy .env.example .env
```

Fill `DEEPSEEK_API_KEY` in `backend/.env`, then start the API:

```bash
uvicorn app.app:app --reload
```

Main endpoint:

```text
POST /api/jobs/optimize
```

Request fields:

- `job_description`: target JD text
- `resume_text`: current resume text
- `language`: `zh` or `en`
- `user_id`: optional metadata, not used for auth in the MVP
$body = @{
  job_description = "岗位名称：AI Agent 应用开发工程师;岗位职责：Agent系统研发：负责基于主流大语言模型（LLM）的 Agent 系统的架构设计、核心功能开发与性能优化。工作流与协同设计：设计并实现多 Agent 协同工作流、任务拆解规划（Planning）以及工具调用（Tool Use/Function Calling）机制。知识检索构建：设计、开发和优化检索增强生成（RAG）系统，包括文档解析、向量化、检索策略优化等，提升 Agent 决策的数据支撑能力。技术跟进与转化：跟踪学术界和工业界在 Agent、LLM 领域的最新技术进展（如新型记忆机制、推理框架等），并结合业务场景进行技术可行性评估与落地。跨部门协同：与产品经理、算法工程师、前端工程师紧密配合，理解业务痛点，将业务逻辑抽象并转化为高效的 Agent 应用。任职要求：专业与学历：计算机、软件工程、人工智能等相关专业本科及以上学历，具备扎实的计算机基础知识。编程能力：熟练掌握 Python、Go 或 Java 等至少一种主流开发语言，具备良好的代码规范和系统设计能力。LLM与框架经验：熟悉大语言模型的基本工作原理，有实际对接国内外主流模型（如 OpenAI、Claude、Qwen、LLaMA 等）API 的开发经验。熟悉至少一种 LLM 开发或 Agent 编排框架（如 LangChain、LlamaIndex、AutoGen、CrewAI、Flowise 等）。数据与检索：熟悉至少一种向量数据库（如 Milvus、Pinecone、Chroma 等）的使用，理解基础的文本向量化（Embedding）与相似度检索原理。工程素养：熟悉常用的后端开发框架与微服务架构，具备良好的调试、性能分析和排查问题的能力。团队协作：具备良好的逻辑思维能力、自驱力、沟通能力以及团队协作精神。加分项：有实际落地并投入生产环境使用的 Agent 或 RAG 项目经验者优先。深入阅读过主流 Agent 框架源码，或在 GitHub 相关开源项目中有贡献者优先。熟悉 Prompt 工程，在 Prompt 调优、防注入、长文本处理等方面有实践经验者优先。了解模型微调（Fine-tuning）基本流程及 LoRA 等常用微调技术者优先。"
  resume_text = "专业技能：编程语言：熟悉 Python，理解常用的数据结构、算法及面向对象设计模式；了解 Go/Shell。Web 框架：熟练掌握 FastAPI、Django、Flask 等 Web 开发框架，具备 RESTful API 设计与开发经验。数据库：熟悉 MySQL 数据库的设计、常用优化（如索引优化、查询优化）；熟悉 Redis 的常用数据结构及缓存应用场景。异步与消息队列：熟悉 Celery、RabbitMQ 的基本使用，具备处理异步任务与削峰限流的实践经验。开发工具与环境：熟练使用 Git 进行版本控制；熟悉 Linux 常用命令及 Docker 容器化部署；了解基本的 CI/CD 流程。工作经历：北京某科技有限公司 | Python 后端开发工程师2022年7月 - 至今（约2年）工作描述：负责公司核心电商/Saas 系统的后端 API 设计、开发与维护。参与数据库表结构的设计与优化，解决日常生产环境中的数据查询延迟问题。配合前端与测试团队，完成功能联调、单元测试及 Bug 修复，保障版本按时上线。上海某信息技术有限公司 | 初级 Python 开发工程师2021年7月 - 2022年6月（1年）工作描述：负责内部运营管理系统（CRM）的基础模块开发与日常维护。编写数据清洗与定时导入脚本，协助数据分析部门进行报表统计。参与编写项目技术文档，协助团队进行日常代码重构。项目经验：项目一：高并发电商系统订单与库存模块项目描述：该项目是公司核心的电商交易系统，随着用户量增长，订单处理和库存控制面临较大并发压力。技术栈：FastAPI + MySQL + Redis + Celery + Docker个人职责与实现：使用 FastAPI 重新设计并实现了订单创建与支付回调接口，提升了接口的响应速度。利用 Redis 分布式锁 机制，处理高并发场景下的商品超卖问题，保障了库存数据的准确性。将耗时的发票生成、邮件通知等业务逻辑设计为异步任务，通过 Celery 队列进行异步处理，降低了主流程的延迟。对部分慢查询 SQL 进行了优化（如合理添加联合索引、优化关联查询），使相关接口的响应时间有所改善。项目二：企业级资产管理系统（EAM）项目描述：针对企业内部资产采购、领用、折旧及盘点流程的管理系统，旨在实现资产全生命周期数字化管理。技术栈：Django + PostgreSQL + Redis + AdminLTE个人职责与实现：基于 Django 框架开发了资产领用审批流、资产台账、权限控制（RBAC）等核心模块。设计了复杂的多表关联结构，并使用 Django ORM 的 select_related 和 prefetch_related 减少了数据库查询次数（N+1问题）。利用 Redis 缓存常用配置项和用户权限数据，减少对主库的频繁读取。编写了数据导入导出工具，支持大批量 Excel 格式的资产数据解析与异步入库，并做好了异常捕获和数据回滚处理。教育背景：[大学名称] | 计算机科学与技术 | 本科2017年9月 - 2021年6月"
  language = "zh"
  user_id = "local"
} | ConvertTo-Json

Invoke-RestMethod `
  -Uri "http://127.0.0.1:8000/api/jobs/optimize" `
  -Method Post `
  -ContentType "application/json" `
  -Body $body
  