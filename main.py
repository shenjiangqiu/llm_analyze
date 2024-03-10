# %%
import tools
from transformers import (
    BertTokenizer,
    BertModel,
    GPT2Tokenizer,
    GPT2Model,
    LlamaTokenizer,
    LlamaModel,
)
import polars as pl

# %% [markdown]
# %%
model = LlamaModel.from_pretrained("meta-llama/Llama-2-7b-hf")
# %%
