from moralis import evm_api
import streamlit as st
import pandas as pd 
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.environ['MORALIS_API_KEY']

st.header('Get NFT data', )
contract_address = st.sidebar.text_input("Contract address")

st.subheader('Get NFT contract data')
def get_data(address):
    if not address:
        st.write('Input Contract Address')
    else:
        result = evm_api.nft.get_nft_contract_transfers(
            api_key = api_key,
            params = {
                "address" : address,
                "chain" : 'eth'
            }
        )
        df = pd.json_normalize(result['result'])
        # st.dataframe(df)
        df = df[df['value'] != '0']
        return df

nft_df = get_data(contract_address)
st.dataframe(nft_df)