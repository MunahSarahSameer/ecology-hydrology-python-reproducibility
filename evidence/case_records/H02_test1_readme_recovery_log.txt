H02 README DEPENDENCY RECOVERY
Python: C:\Users\REDACTED_USER\miniconda3\envs\code_decay\python.exe
Packages requested: ['einops', 'timm', 'opencv-python', 'tensorboard', 'torchmetrics']
Installation exit code: 0
Installation output:
Collecting einops
  Downloading einops-0.8.2-py3-none-any.whl.metadata (13 kB)
Collecting timm
  Downloading timm-1.0.31-py3-none-any.whl.metadata (42 kB)
Collecting opencv-python
  Using cached opencv_python-5.0.0.93-cp37-abi3-win_amd64.whl.metadata (20 kB)
Collecting tensorboard
  Downloading tensorboard-2.21.0-py3-none-any.whl.metadata (1.8 kB)
Collecting torchmetrics
  Downloading torchmetrics-1.9.0-py3-none-any.whl.metadata (23 kB)
Requirement already satisfied: torch in C:\Users\REDACTED_USER\miniconda3\envs\code_decay\Lib\site-packages (from timm) (2.15.0+cpu)
Collecting torchvision (from timm)
  Downloading torchvision-0.29.2-py3-none-win_amd64.whl.metadata (5.7 kB)
Requirement already satisfied: pyyaml in C:\Users\REDACTED_USER\miniconda3\envs\code_decay\Lib\site-packages (from timm) (6.0.3)
Collecting huggingface_hub (from timm)
  Downloading huggingface_hub-2.4.0-py3-none-any.whl.metadata (16 kB)
Collecting safetensors (from timm)
  Downloading safetensors-0.8.0-cp310-abi3-win_amd64.whl.metadata (4.2 kB)
Requirement already satisfied: numpy>=2 in C:\Users\REDACTED_USER\miniconda3\envs\code_decay\Lib\site-packages (from opencv-python) (2.4.6)
Collecting absl-py>=0.4 (from tensorboard)
  Downloading absl_py-2.5.1-py3-none-any.whl.metadata (3.3 kB)
Collecting grpcio<2.0,>=1.74.0 (from tensorboard)
  Downloading grpcio-1.85.1-cp311-cp311-win_amd64.whl.metadata (3.9 kB)
Collecting markdown>=2.6.8 (from tensorboard)
  Downloading markdown-3.11.3-py3-none-any.whl.metadata (5.1 kB)
Requirement already satisfied: packaging in C:\Users\REDACTED_USER\miniconda3\envs\code_decay\Lib\site-packages (from tensorboard) (26.3)
Requirement already satisfied: pillow in C:\Users\REDACTED_USER\miniconda3\envs\code_decay\Lib\site-packages (from tensorboard) (12.2.0)
Collecting protobuf<8.0.0,>=6.31.1 (from tensorboard)
  Downloading protobuf-7.36.2-cp310-abi3-win_amd64.whl.metadata (595 bytes)
Requirement already satisfied: setuptools>=41.0.0 in C:\Users\REDACTED_USER\miniconda3\envs\code_decay\Lib\site-packages (from tensorboard) (84.2.1)
Collecting tensorboard-data-server<0.8.0,>=0.7.0 (from tensorboard)
  Downloading tensorboard_data_server-0.7.2-py3-none-any.whl.metadata (1.1 kB)
Collecting werkzeug>=1.0.1 (from tensorboard)
  Downloading werkzeug-3.1.9-py3-none-any.whl.metadata (4.1 kB)
Requirement already satisfied: typing-extensions~=4.12 in C:\Users\REDACTED_USER\miniconda3\envs\code_decay\Lib\site-packages (from grpcio<2.0,>=1.74.0->tensorboard) (4.16.0)
Collecting lightning-utilities>=0.15.3 (from torchmetrics)
  Downloading lightning_utilities-0.15.3-py3-none-any.whl.metadata (5.5 kB)
Requirement already satisfied: filelock in C:\Users\REDACTED_USER\miniconda3\envs\code_decay\Lib\site-packages (from torch->timm) (4.2.4)
Requirement already satisfied: sympy>=1.13.3 in C:\Users\REDACTED_USER\miniconda3\envs\code_decay\Lib\site-packages (from torch->timm) (1.14.0)
Requirement already satisfied: networkx>=2.5.1 in C:\Users\REDACTED_USER\miniconda3\envs\code_decay\Lib\site-packages (from torch->timm) (3.6.1)
Requirement already satisfied: jinja2 in C:\Users\REDACTED_USER\miniconda3\envs\code_decay\Lib\site-packages (from torch->timm) (3.1.6)
Requirement already satisfied: fsspec>=0.8.5 in C:\Users\REDACTED_USER\miniconda3\envs\code_decay\Lib\site-packages (from torch->timm) (2026.9.0)
Requirement already satisfied: mpmath<1.4,>=1.1.0 in C:\Users\REDACTED_USER\miniconda3\envs\code_decay\Lib\site-packages (from sympy>=1.13.3->torch->timm) (1.3.0)
Requirement already satisfied: markupsafe>=2.1.1 in C:\Users\REDACTED_USER\miniconda3\envs\code_decay\Lib\site-packages (from werkzeug>=1.0.1->tensorboard) (3.0.3)
Requirement already satisfied: click<9.0.0,>=8.4.2 in C:\Users\REDACTED_USER\miniconda3\envs\code_decay\Lib\site-packages (from huggingface_hub->timm) (8.5.1)
Collecting hf-xet<2.0.0,>=1.6.0 (from huggingface_hub->timm)
  Downloading hf_xet-1.8.0-cp38-abi3-win_amd64.whl.metadata (4.9 kB)
Collecting httpx2<3,>=2.0.0 (from huggingface_hub->timm)
  Downloading httpx2-2.16.0-py3-none-any.whl.metadata (10 kB)
Requirement already satisfied: tqdm>=4.42.1 in C:\Users\REDACTED_USER\miniconda3\envs\code_decay\Lib\site-packages (from huggingface_hub->timm) (4.70.1)
Requirement already satisfied: anyio>=4.10 in C:\Users\REDACTED_USER\miniconda3\envs\code_decay\Lib\site-packages (from httpx2<3,>=2.0.0->huggingface_hub->timm) (4.15.1)
Collecting httpcore2==2.16.0 (from httpx2<3,>=2.0.0->huggingface_hub->timm)
  Downloading httpcore2-2.16.0-py3-none-any.whl.metadata (27 kB)
Requirement already satisfied: idna>=3.18 in C:\Users\REDACTED_USER\miniconda3\envs\code_decay\Lib\site-packages (from httpx2<3,>=2.0.0->huggingface_hub->timm) (3.20)
Collecting truststore>=0.10 (from httpx2<3,>=2.0.0->huggingface_hub->timm)
  Downloading truststore-0.10.5-py3-none-any.whl.metadata (4.5 kB)
Requirement already satisfied: h11>=0.16 in C:\Users\REDACTED_USER\miniconda3\envs\code_decay\Lib\site-packages (from httpcore2==2.16.0->httpx2<3,>=2.0.0->huggingface_hub->timm) (0.16.0)
Requirement already satisfied: colorama in C:\Users\REDACTED_USER\miniconda3\envs\code_decay\Lib\site-packages (from tqdm>=4.42.1->huggingface_hub->timm) (0.4.6)
Downloading einops-0.8.2-py3-none-any.whl (65 kB)
Downloading timm-1.0.31-py3-none-any.whl (2.8 MB)
   ---------------------------------------- 0.0/2.8 MB ? eta -:--:--
   -------------------------- ------------- 1.8/2.8 MB 10.1 MB/s eta 0:00:01
   ---------------------------------------- 2.8/2.8 MB 10.8 MB/s  0:00:00
Using cached opencv_python-5.0.0.93-cp37-abi3-win_amd64.whl (44.0 MB)
Downloading tensorboard-2.21.0-py3-none-any.whl (5.5 MB)
   ---------------------------------------- 0.0/5.5 MB ? eta -:--:--
   -------------------- ------------------- 2.9/5.5 MB 14.0 MB/s eta 0:00:01
   ---------------------------------- ----- 4.7/5.5 MB 11.4 MB/s eta 0:00:01
   ---------------------------------------- 5.5/5.5 MB 10.9 MB/s  0:00:00
Downloading grpcio-1.85.1-cp311-cp311-win_amd64.whl (5.6 MB)
   ---------------------------------------- 0.0/5.6 MB ? eta -:--:--
   ---------------------------- ----------- 3.9/5.6 MB 21.5 MB/s eta 0:00:01
   ---------------------------------------- 5.6/5.6 MB 19.1 MB/s  0:00:00
Downloading protobuf-7.36.2-cp310-abi3-win_amd64.whl (456 kB)
Downloading tensorboard_data_server-0.7.2-py3-none-any.whl (2.4 kB)
Downloading torchmetrics-1.9.0-py3-none-any.whl (983 kB)
   ---------------------------------------- 0.0/983.4 kB ? eta -:--:--
   ---------------------------------------- 983.4/983.4 kB 22.5 MB/s  0:00:00
Downloading absl_py-2.5.1-py3-none-any.whl (137 kB)
Downloading lightning_utilities-0.15.3-py3-none-any.whl (31 kB)
Downloading markdown-3.11.3-py3-none-any.whl (116 kB)
Downloading werkzeug-3.1.9-py3-none-any.whl (228 kB)
Downloading huggingface_hub-2.4.0-py3-none-any.whl (857 kB)
   ---------------------------------------- 0.0/857.0 kB ? eta -:--:--
   ---------------------------------------- 857.0/857.0 kB 12.7 MB/s  0:00:00
Downloading hf_xet-1.8.0-cp38-abi3-win_amd64.whl (3.9 MB)
   ---------------------------------------- 0.0/3.9 MB ? eta -:--:--
   ----------------------------- ---------- 2.9/3.9 MB 15.2 MB/s eta 0:00:01
   ---------------------------------------- 3.9/3.9 MB 13.7 MB/s  0:00:00
Downloading httpx2-2.16.0-py3-none-any.whl (97 kB)
Downloading httpcore2-2.16.0-py3-none-any.whl (85 kB)
Downloading truststore-0.10.5-py3-none-any.whl (19 kB)
Downloading safetensors-0.8.0-cp310-abi3-win_amd64.whl (355 kB)
Downloading torchvision-0.29.2-py3-none-win_amd64.whl (1.4 MB)
   ---------------------------------------- 0.0/1.4 MB ? eta -:--:--
   ---------------------------------------- 1.4/1.4 MB 23.8 MB/s  0:00:00
Installing collected packages: werkzeug, truststore, tensorboard-data-server, safetensors, protobuf, opencv-python, markdown, lightning-utilities, hf-xet, grpcio, einops, absl-py, tensorboard, httpcore2, torchvision, torchmetrics, httpx2, huggingface_hub, timm

   ----------------------------------------  0/19 [werkzeug]
   ----------------------------------------  0/19 [werkzeug]
   ------ ---------------------------------  3/19 [safetensors]
   -------- -------------------------------  4/19 [protobuf]
   -------- -------------------------------  4/19 [protobuf]
   -------- -------------------------------  4/19 [protobuf]
   ---------- -----------------------------  5/19 [opencv-python]
   ---------- -----------------------------  5/19 [opencv-python]
   ---------- -----------------------------  5/19 [opencv-python]
   ------------ ---------------------------  6/19 [markdown]
   ------------ ---------------------------  6/19 [markdown]
   ------------------ ---------------------  9/19 [grpcio]
   ------------------ ---------------------  9/19 [grpcio]
   --------------------- ------------------ 10/19 [einops]
   ----------------------- ---------------- 11/19 [absl-py]
   ------------------------- -------------- 12/19 [tensorboard]
   ------------------------- -------------- 12/19 [tensorboard]
   ------------------------- -------------- 12/19 [tensorboard]
   ------------------------- -------------- 12/19 [tensorboard]
   ------------------------- -------------- 12/19 [tensorboard]
   ------------------------- -------------- 12/19 [tensorboard]
   ------------------------- -------------- 12/19 [tensorboard]
   ------------------------- -------------- 12/19 [tensorboard]
   ------------------------- -------------- 12/19 [tensorboard]
   --------------------------- ------------ 13/19 [httpcore2]
   ----------------------------- ---------- 14/19 [torchvision]
   ----------------------------- ---------- 14/19 [torchvision]
   ----------------------------- ---------- 14/19 [torchvision]
   ----------------------------- ---------- 14/19 [torchvision]
   ----------------------------- ---------- 14/19 [torchvision]
   ------------------------------- -------- 15/19 [torchmetrics]
   ------------------------------- -------- 15/19 [torchmetrics]
   ------------------------------- -------- 15/19 [torchmetrics]
   ------------------------------- -------- 15/19 [torchmetrics]
   ------------------------------- -------- 15/19 [torchmetrics]
   ------------------------------- -------- 15/19 [torchmetrics]
   ------------------------------- -------- 15/19 [torchmetrics]
   ------------------------------- -------- 15/19 [torchmetrics]
   ------------------------------- -------- 15/19 [torchmetrics]
   ------------------------------- -------- 15/19 [torchmetrics]
   --------------------------------- ------ 16/19 [httpx2]
   ----------------------------------- ---- 17/19 [huggingface_hub]
   ----------------------------------- ---- 17/19 [huggingface_hub]
   ----------------------------------- ---- 17/19 [huggingface_hub]
   ----------------------------------- ---- 17/19 [huggingface_hub]
   ----------------------------------- ---- 17/19 [huggingface_hub]
   ----------------------------------- ---- 17/19 [huggingface_hub]
   ----------------------------------- ---- 17/19 [huggingface_hub]
   ------------------------------------- -- 18/19 [timm]
   ------------------------------------- -- 18/19 [timm]
   ------------------------------------- -- 18/19 [timm]
   ------------------------------------- -- 18/19 [timm]
   ------------------------------------- -- 18/19 [timm]
   ------------------------------------- -- 18/19 [timm]
   ------------------------------------- -- 18/19 [timm]
   ------------------------------------- -- 18/19 [timm]
   ------------------------------------- -- 18/19 [timm]
   ------------------------------------- -- 18/19 [timm]
   ------------------------------------- -- 18/19 [timm]
   ------------------------------------- -- 18/19 [timm]
   ---------------------------------------- 19/19 [timm]

Successfully installed absl-py-2.5.1 einops-0.8.2 grpcio-1.85.1 hf-xet-1.8.0 httpcore2-2.16.0 httpx2-2.16.0 huggingface_hub-2.4.0 lightning-utilities-0.15.3 markdown-3.11.3 opencv-python-5.0.0.93 protobuf-7.36.2 safetensors-0.8.0 tensorboard-2.21.0 tensorboard-data-server-0.7.2 timm-1.0.31 torchmetrics-1.9.0 torchvision-0.29.2 truststore-0.10.5 werkzeug-3.1.9


Retest exit code: 0
Retest runtime: 11.58

STDOUT:
usage: run_test.py [-h] [--shard_id SHARD_ID] [--num_shards NUM_SHARDS]
                   [--init_method INIT_METHOD] [--cfg CFG_FILE]
                   ...

Provide FloodSformer training and testing pipeline.

positional arguments:
  opts                  See floodsformer/config/defaults.py for all options

options:
  -h, --help            show this help message and exit
  --shard_id SHARD_ID   The shard id of current node, Starts from 0 to
                        num_shards - 1
  --num_shards NUM_SHARDS
                        Number of shards using by the job
  --init_method INIT_METHOD
                        Initialization method, includes TCP or shared file-
                        system
  --cfg CFG_FILE        Path to the config file


STDERR:
C:\Users\REDACTED_USER\miniconda3\envs\code_decay\Lib\site-packages\timm\models\layers\__init__.py:49: FutureWarning: Importing from timm.models.layers is deprecated, please import via timm.layers
  warnings.warn(f"Importing from {__name__} is deprecated, please import via timm.layers", FutureWarning)

