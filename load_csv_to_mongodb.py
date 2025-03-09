# Step 1: Load CSV data into MongoDB
from langchain.chains import LLMChain
from langchain.llms import HuggingFacePipeline
from langchain.prompts import PromptTemplate
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline


def load_csv_to_mongodb(C:\Users\vinay\Downloads\aal\sample_data.csv , db_name, collection_name, mongo_uri="mongodb://localhost:27017/"):
    """
    Load CSV data into MongoDB.
    """
    # Read CSV file
    df = pd.read_csv(csv_file)

    # Connect to MongoDB
    client = MongoClient(mongo_uri)
    db = client[mongo]
    collection = db[products]

    # Insert data into MongoDB
    records = df.to_dict("records")
    collection.insert_many(records)
    print(f"Data loaded into MongoDB collection '{collection_name}'.")

# Step 2: Generate MongoDB query using LLM
def generate_mongodb_query(user_input, column_name):
    """
    Generate a MongoDB query using an open-source LLM.
    """
    # Load an open-source LLM (e.g., GPT-Neo)
    model_name = "EleutherAI/gpt-neo-1.3B"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    pipe = pipeline("text-generation", model=model, tokenizer=tokenizer, max_length=100)
    llm = HuggingFacePipeline(pipeline=pipe)

    # Define prompt template
    prompt_template = PromptTemplate(
        input_variables=["user_input", "column_name"],
        template="Generate a MongoDB query to {user_input} for the column '{column_name}'."
    )

    # Create LLM chain
    chain = LLMChain(llm=llm, prompt=prompt_template)
    query = chain.run(user_input=user_input, column_name=column_name)
    return query