import streamlit as st
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraphagenticai.LLMs.groq_llm import GROQLLM
from src.langgraphagenticai.graph.graphicbuilder import graphbuilder
from src.langgraphagenticai.ui.streamlitui.display_result import DisplayResultStreamlit


def load_langgraph_agentic_ai_ui():
    """
    Loads and runs the LangGraph Agentic AO applications with streamlit ui.
    this fucntion initializes the UI and handles user input, configures the LLM model,
    sets up the graoh based on the selected use case, and displays the output while
    implementing error handling for robutness.
    """

    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()
    if not user_input:
        st.error("Failed to load user input. Please try again.")
        return
    user_message = st.chat_input("Enter your message here:")

    if user_message:
        try:
            ##configuring the llms
            obj_llm_config = GROQLLM(user_control_input=user_input)
            model = obj_llm_config.get_llm_model()
            if not model:
                st.error("Failed to initialize the LLM model. Please check your configuration.")
                return
            #setting up the graph based on usecase
            usecase = user_input.get("selected_usecase")
            if not usecase:
                st.error("No use case selected.")
                return
            ##graph builder
            graph_builder = graphbuilder(model)
            try:
                graph = graph_builder.setup_graph(usecase)
                DisplayResultStreamlit(usecase, graph, user_message).display_result_on_ui()
            except Exception as e:
                st.error(f"Error setting up the graph: {e}")
                return
        except Exception as e:
            st.error(f"An error occurred: {e}")
            return