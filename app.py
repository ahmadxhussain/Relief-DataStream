import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, date
import json
import os
from typing import Dict, List, Optional, Tuple
import random
from translations import get_translation, get_supported_languages
from api_service import api_service
from config import get_config
from report_generator import download_pdf_report, download_docx_report

# Page configuration
st.set_page_config(
    page_title="NGO Data Helpers",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling (works with Streamlit's native theming)
def get_css():
    """Get CSS for custom components"""
    return """
    <style>
        .main-header {
            font-size: 2.5rem;
            font-weight: bold;
            text-align: center;
            margin-bottom: 2rem;
        }
        .section-header {
            font-size: 1.5rem;
            font-weight: 600;
            margin-top: 2rem;
            margin-bottom: 1rem;
        }
        .metric-card {
            padding: 1rem;
            border-radius: 0.5rem;
            border-left: 4px solid #3b82f6;
            margin-bottom: 1rem;
        }
        .error-message {
            background-color: #fef2f2;
            border: 1px solid #fecaca;
            color: #dc2626;
            padding: 1rem;
            border-radius: 0.5rem;
            margin-bottom: 1rem;
        }
        .success-message {
            background-color: #f0fdf4;
            border: 1px solid #bbf7d0;
            color: #16a34a;
            padding: 1rem;
            border-radius: 0.5rem;
            margin-bottom: 1rem;
        }
    </style>
    """

# Initialize session state
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'home'
if 'selected_country' not in st.session_state:
    st.session_state.selected_country = None
if 'date_range' not in st.session_state:
    st.session_state.date_range = None
if 'report_data' not in st.session_state:
    st.session_state.report_data = None
if 'is_loading' not in st.session_state:
    st.session_state.is_loading = False
if 'progress_steps' not in st.session_state:
    st.session_state.progress_steps = [
        {'id': 'collecting', 'label': 'step_collecting', 'completed': False, 'active': False},
        {'id': 'processing', 'label': 'step_processing', 'completed': False, 'active': False},
        {'id': 'summarizing', 'label': 'step_summarizing', 'completed': False, 'active': False},
        {'id': 'ready', 'label': 'step_ready', 'completed': False, 'active': False}
    ]
if 'current_step' not in st.session_state:
    st.session_state.current_step = 0
if 'error_message' not in st.session_state:
    st.session_state.error_message = None
if 'current_language' not in st.session_state:
    st.session_state.current_language = 'en'
if 'saved_reports' not in st.session_state:
    st.session_state.saved_reports = []

# Get countries from API service
COUNTRIES = api_service.fetch_countries()

# Apply CSS after session state is initialized
st.markdown(get_css(), unsafe_allow_html=True)

def generate_mock_report_data(country: Dict, date_range: Dict) -> Dict:
    """Generate mock report data similar to React version"""
    chart_data = [
        {'name': 'Jan', 'value': random.randint(20, 120), 'date': '2024-01-01'},
        {'name': 'Feb', 'value': random.randint(20, 120), 'date': '2024-02-01'},
        {'name': 'Mar', 'value': random.randint(20, 120), 'date': '2024-03-01'},
        {'name': 'Apr', 'value': random.randint(20, 120), 'date': '2024-04-01'},
        {'name': 'May', 'value': random.randint(20, 120), 'date': '2024-05-01'},
        {'name': 'Jun', 'value': random.randint(20, 120), 'date': '2024-06-01'},
    ]
    
    return {
        'summary': f"This report provides an analysis of humanitarian and development indicators for {country['name']} from {date_range['start_date']} to {date_range['end_date']}. The data shows significant variations in key metrics, with particular attention to economic stability, social development, and humanitarian needs.",
        'key_events': [
            f"Major policy changes announced in {country['name']} affecting development priorities",
            "International aid programs launched targeting vulnerable populations",
            "Economic indicators show mixed results with some sectors improving",
            "New partnerships established with local NGOs and government agencies",
            "Climate-related challenges continue to impact rural communities"
        ],
        'trends': [
            "Gradual improvement in education access indicators",
            "Healthcare infrastructure showing positive development",
            "Economic stability remains a concern in certain regions",
            "Technology adoption increasing among youth populations",
            "Environmental sustainability initiatives gaining momentum"
        ],
        'risks': [
            "Political instability may affect ongoing development programs",
            "Economic volatility could impact funding availability",
            "Climate change continues to pose significant challenges",
            "Resource constraints may limit program expansion",
            "Security concerns in certain regions affecting aid delivery"
        ],
        'chart_data': chart_data
    }

def show_error(message: str):
    """Display error message"""
    st.session_state.error_message = message

def clear_error():
    """Clear error message"""
    st.session_state.error_message = None

def reset_form():
    """Reset form data"""
    st.session_state.selected_country = None
    st.session_state.date_range = None
    st.session_state.report_data = None
    st.session_state.is_loading = False
    st.session_state.current_step = 0
    st.session_state.progress_steps = [
        {'id': 'collecting', 'label': 'step_collecting', 'completed': False, 'active': False},
        {'id': 'processing', 'label': 'step_processing', 'completed': False, 'active': False},
        {'id': 'summarizing', 'label': 'step_summarizing', 'completed': False, 'active': False},
        {'id': 'ready', 'label': 'step_ready', 'completed': False, 'active': False}
    ]
    clear_error()

def build_report():
    """Simulate report building process"""
    if not st.session_state.selected_country or not st.session_state.date_range:
        show_error(get_translation(st.session_state.current_language, 'error_country_dates'))
        return
    
    st.session_state.is_loading = True
    st.session_state.current_step = 0
    
    # Simulate progress steps
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    steps = ['step_collecting', 'step_processing', 'step_summarizing', 'step_ready']
    
    for i, step in enumerate(steps):
        status_text.text(f"Status: {get_translation(st.session_state.current_language, step)}")
        progress_bar.progress((i + 1) / len(steps))
        
        # Update progress steps
        for j, progress_step in enumerate(st.session_state.progress_steps):
            progress_step['completed'] = j <= i
            progress_step['active'] = j == i + 1
        
        st.session_state.current_step = i + 1
        
        # Simulate processing time
        import time
        time.sleep(1)
    
    # Get report data from API service
    try:
        report_response = api_service.generate_report(
            st.session_state.selected_country,
            st.session_state.date_range
        )
        
        if 'error' in report_response:
            show_error(report_response['error'])
            st.session_state.is_loading = False
            return
        
        report_id = report_response['report_id']
        report_data = api_service.get_report_data(report_id)
        
        if report_data and 'error' not in report_data:
            st.session_state.report_data = report_data
        else:
            # Fallback to mock data
            st.session_state.report_data = generate_mock_report_data(
                st.session_state.selected_country,
                st.session_state.date_range
            )
    
    except Exception as e:
        # Fallback to mock data on error
        st.session_state.report_data = generate_mock_report_data(
            st.session_state.selected_country,
            st.session_state.date_range
        )
    
    # Save to history
    report_id = str(datetime.now().timestamp())
    saved_report = {
        'id': report_id,
        'country': st.session_state.selected_country,
        'date_range': st.session_state.date_range,
        'report_data': st.session_state.report_data,
        'created_at': datetime.now().isoformat(),
        'title': f"{st.session_state.selected_country['name']} Report - {st.session_state.date_range['start_date']} to {st.session_state.date_range['end_date']}"
    }
    
    st.session_state.saved_reports.append(saved_report)
    
    st.session_state.is_loading = False
    st.session_state.current_page = 'preview'
    
    progress_bar.empty()
    status_text.empty()

def render_home_page():
    """Render the home page"""
    st.markdown(f'<h1 class="main-header">🌍 {get_translation(st.session_state.current_language, "app_title")}</h1>', unsafe_allow_html=True)
    st.markdown(f'<p style="text-align: center; color: #6b7280; margin-bottom: 2rem;">{get_translation(st.session_state.current_language, "app_subtitle")}</p>', unsafe_allow_html=True)
    
    # Error message
    if st.session_state.error_message:
        st.markdown(f'<div class="error-message">⚠️ {st.session_state.error_message}</div>', unsafe_allow_html=True)
        if st.button(get_translation(st.session_state.current_language, "dismiss"), key="dismiss_error"):
            clear_error()
    
    # Main form
    with st.container():
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown(f'<h3 class="section-header">📍 {get_translation(st.session_state.current_language, "select_country")}</h3>', unsafe_allow_html=True)
            country_options = [''] + [f"{c['name']} ({c['code']})" for c in COUNTRIES]
            selected_country_str = st.selectbox(
                get_translation(st.session_state.current_language, "select_country_placeholder"),
                options=country_options,
                index=0,
                disabled=st.session_state.is_loading,
                key="country_select"
            )
            
            if selected_country_str:
                country_code = selected_country_str.split('(')[1].split(')')[0]
                country_name = selected_country_str.split(' (')[0]
                st.session_state.selected_country = {'code': country_code, 'name': country_name}
        
        with col2:
            st.markdown(f'<h3 class="section-header">📅 {get_translation(st.session_state.current_language, "select_date_range")}</h3>', unsafe_allow_html=True)
            col_start, col_end = st.columns(2)
            
            with col_start:
                start_date = st.date_input(
                    f"{get_translation(st.session_state.current_language, 'start_date')}:",
                    value=date(2024, 1, 1),
                    disabled=st.session_state.is_loading,
                    key="start_date"
                )
            
            with col_end:
                end_date = st.date_input(
                    f"{get_translation(st.session_state.current_language, 'end_date')}:",
                    value=date(2024, 6, 30),
                    disabled=st.session_state.is_loading,
                    key="end_date"
                )
            
            if start_date and end_date:
                st.session_state.date_range = {
                    'start_date': start_date.strftime('%Y-%m-%d'),
                    'end_date': end_date.strftime('%Y-%m-%d')
                }
    
    # Action buttons
    st.markdown('<br>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col2:
        can_build = st.session_state.selected_country and st.session_state.date_range and not st.session_state.is_loading
        button_text = get_translation(st.session_state.current_language, "building") if st.session_state.is_loading else get_translation(st.session_state.current_language, "build_report")
        if st.button(
            f"🚀 {button_text}",
            disabled=not can_build,
            type="primary",
            use_container_width=True
        ):
            build_report()
    
    with col3:
        if st.button(f"🔄 {get_translation(st.session_state.current_language, 'reset')}", disabled=st.session_state.is_loading, use_container_width=True):
            reset_form()
            st.rerun()
    
    # Progress section
    if st.session_state.is_loading:
        st.markdown(f'<h3 class="section-header">📊 {get_translation(st.session_state.current_language, "progress_title")}</h3>', unsafe_allow_html=True)
        
        # Progress steps
        cols = st.columns(4)
        for i, step in enumerate(st.session_state.progress_steps):
            with cols[i]:
                step_text = get_translation(st.session_state.current_language, step['label'])
                if step['completed']:
                    st.markdown(f"✅ **{step_text}**")
                elif step['active']:
                    st.markdown(f"⏳ **{step_text}**")
                else:
                    st.markdown(f"⏸️ {step_text}")

def render_report_preview():
    """Render the report preview page"""
    if not st.session_state.report_data:
        st.error("No report data available. Please generate a report first.")
        if st.button(f"← {get_translation(st.session_state.current_language, 'back_to_home')}"):
            st.session_state.current_page = 'home'
            st.rerun()
        return
    
    # Header
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown(f'<h1 class="main-header">📊 {get_translation(st.session_state.current_language, "report_preview")}</h1>', unsafe_allow_html=True)
    with col2:
        if st.button(f"← {get_translation(st.session_state.current_language, 'back_to_home')}", use_container_width=True):
            st.session_state.current_page = 'home'
            st.rerun()
    
    report = st.session_state.report_data
    
    # Executive Summary
    st.markdown(f'<h2 class="section-header">📋 {get_translation(st.session_state.current_language, "executive_summary")}</h2>', unsafe_allow_html=True)
    st.markdown(f'<div class="metric-card">{report["summary"]}</div>', unsafe_allow_html=True)
    
    # Key Events
    st.markdown(f'<h2 class="section-header">📅 {get_translation(st.session_state.current_language, "key_events")}</h2>', unsafe_allow_html=True)
    for i, event in enumerate(report['key_events'], 1):
        st.markdown(f"**{i}.** {event}")
    
    # Trends
    st.markdown(f'<h2 class="section-header">📈 {get_translation(st.session_state.current_language, "trends")}</h2>', unsafe_allow_html=True)
    for i, trend in enumerate(report['trends'], 1):
        st.markdown(f"**{i}.** {trend}")
    
    # Risks
    st.markdown(f'<h2 class="section-header">⚠️ {get_translation(st.session_state.current_language, "risks")}</h2>', unsafe_allow_html=True)
    for i, risk in enumerate(report['risks'], 1):
        st.markdown(f"**{i}.** {risk}")
    
    # Charts
    st.markdown(f'<h2 class="section-header">📊 {get_translation(st.session_state.current_language, "data_visualization")}</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f'<h4>{get_translation(st.session_state.current_language, "monthly_trends")}</h4>', unsafe_allow_html=True)
        df = pd.DataFrame(report['chart_data'])
        fig_line = px.line(df, x='name', y='value', title=get_translation(st.session_state.current_language, "monthly_trends"))
        fig_line.update_layout(height=400)
        st.plotly_chart(fig_line, use_container_width=True)
    
    with col2:
        st.markdown(f'<h4>{get_translation(st.session_state.current_language, "monthly_comparison")}</h4>', unsafe_allow_html=True)
        fig_bar = px.bar(df, x='name', y='value', title=get_translation(st.session_state.current_language, "monthly_comparison"))
        fig_bar.update_layout(height=400)
        st.plotly_chart(fig_bar, use_container_width=True)
    
    # Download section
    st.markdown(f'<h2 class="section-header">💾 {get_translation(st.session_state.current_language, "download_report")}</h2>', unsafe_allow_html=True)
    st.markdown(f'<p style="color: #6b7280;">{get_translation(st.session_state.current_language, "download_description")}</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Generate and download PDF
        download_pdf_report(
            st.session_state.report_data,
            st.session_state.selected_country['name'],
            st.session_state.date_range
        )
    
    with col2:
        # Generate and download DOCX
        download_docx_report(
            st.session_state.report_data,
            st.session_state.selected_country['name'],
            st.session_state.date_range
        )

def render_help_page():
    """Render the help page"""
    st.markdown(f'<h1 class="main-header">❓ {get_translation(st.session_state.current_language, "help_title")}</h1>', unsafe_allow_html=True)
    
    st.markdown(f'<h2 class="section-header">{get_translation(st.session_state.current_language, "how_to_use")}</h2>', unsafe_allow_html=True)
    st.markdown(f'<p style="color: #6b7280; margin-bottom: 1.5rem;">{get_translation(st.session_state.current_language, "help_description")}</p>', unsafe_allow_html=True)
    
    # Steps
    steps_data = [
        ("📍", "step1_title", "step1_desc"),
        ("🚀", "step2_title", "step2_desc"),
        ("📊", "step3_title", "step3_desc"),
        ("💾", "step4_title", "step4_desc")
    ]
    
    for icon, title_key, desc_key in steps_data:
        st.markdown(f'<div class="metric-card"><strong>{icon} {get_translation(st.session_state.current_language, title_key)}</strong><br>{get_translation(st.session_state.current_language, desc_key)}</div>', unsafe_allow_html=True)
    
    # Features
    st.markdown(f'<h2 class="section-header">{get_translation(st.session_state.current_language, "features_title")}</h2>', unsafe_allow_html=True)
    features_data = [
        ("📋", "feature_reports", "feature_reports_desc"),
        ("📊", "feature_charts", "feature_charts_desc"),
        ("💾", "feature_download", "feature_download_desc"),
        ("🔄", "feature_reset", "feature_reset_desc")
    ]
    
    for icon, title_key, desc_key in features_data:
        st.markdown(f'<div class="metric-card"><strong>{icon} {get_translation(st.session_state.current_language, title_key)}</strong><br>{get_translation(st.session_state.current_language, desc_key)}</div>', unsafe_allow_html=True)
    
    # Troubleshooting
    st.markdown(f'<h2 class="section-header">{get_translation(st.session_state.current_language, "troubleshooting_title")}</h2>', unsafe_allow_html=True)
    troubleshooting_data = [
        ("error_country_dates", "error_country_dates_desc"),
        ("error_build_report", "error_build_report_desc"),
        ("error_download", "error_download_desc")
    ]
    
    for error_key, solution_key in troubleshooting_data:
        st.markdown(f'<div class="metric-card"><strong>⚠️ "{get_translation(st.session_state.current_language, error_key)}"</strong><br>{get_translation(st.session_state.current_language, solution_key)}</div>', unsafe_allow_html=True)
    
    # About
    st.markdown(f'<h2 class="section-header">{get_translation(st.session_state.current_language, "about_title")}</h2>', unsafe_allow_html=True)
    st.markdown(f'<p style="color: #6b7280;">{get_translation(st.session_state.current_language, "about_desc")}</p>', unsafe_allow_html=True)
    st.markdown(f'<p style="color: #6b7280; font-size: 0.875rem;">{get_translation(st.session_state.current_language, "about_note")}</p>', unsafe_allow_html=True)

def render_settings_page():
    """Render the settings page"""
    st.markdown(f'<h1 class="main-header">⚙️ {get_translation(st.session_state.current_language, "settings_title")}</h1>', unsafe_allow_html=True)
    
    # Language Settings
    st.markdown(f'<h2 class="section-header">{get_translation(st.session_state.current_language, "language_settings")}</h2>', unsafe_allow_html=True)
    
    languages = get_supported_languages()
    
    language_options = [f"{lang['flag']} {lang['name']}" for lang in languages]
    current_lang = next((lang for lang in languages if lang['code'] == st.session_state.current_language), languages[0])
    current_index = languages.index(current_lang)
    
    selected_language = st.selectbox(
        f"{get_translation(st.session_state.current_language, 'select_language')}",
        options=language_options,
        index=current_index,
        key="language_select"
    )
    
    if selected_language:
        selected_code = languages[language_options.index(selected_language)]['code']
        if selected_code != st.session_state.current_language:
            st.session_state.current_language = selected_code
            st.rerun()
    
    # Theme Information
    st.markdown(f'<h2 class="section-header">{get_translation(st.session_state.current_language, "theme_settings")}</h2>', unsafe_allow_html=True)
    st.info("🎨 " + get_translation(st.session_state.current_language, "theme_info_desc") + " Use the hamburger menu (☰) in the top-right corner to switch between light and dark themes.")
    
    # Language Information
    st.markdown(f'<h2 class="section-header">{get_translation(st.session_state.current_language, "language_info")}</h2>', unsafe_allow_html=True)
    
    for lang in languages:
        st.markdown(f'<div class="metric-card"><strong>{lang["flag"]} {lang["name"]}</strong><br>{get_translation(st.session_state.current_language, "language_info_desc")}</div>', unsafe_allow_html=True)

def render_history_page():
    """Render the history page"""
    st.markdown(f'<h1 class="main-header">📚 {get_translation(st.session_state.current_language, "history_title")}</h1>', unsafe_allow_html=True)
    
    if not st.session_state.saved_reports:
        st.markdown(f'<div class="metric-card" style="text-align: center; padding: 3rem;"><h3 style="color: #6b7280;">{get_translation(st.session_state.current_language, "no_reports")}</h3><p style="color: #9ca3af;">{get_translation(st.session_state.current_language, "no_reports_desc")}</p></div>', unsafe_allow_html=True)
        if st.button(f"← {get_translation(st.session_state.current_language, 'back_to_home')}"):
            st.session_state.current_page = 'home'
            st.rerun()
        return
    
    # Search functionality
    search_term = st.text_input(f"🔍 {get_translation(st.session_state.current_language, 'search_reports')}", placeholder=get_translation(st.session_state.current_language, "search_placeholder"))
    
    # Filter reports
    filtered_reports = st.session_state.saved_reports
    if search_term:
        filtered_reports = [
            report for report in st.session_state.saved_reports
            if (search_term.lower() in report['country']['name'].lower() or
                search_term.lower() in report['title'].lower() or
                search_term in report['date_range']['start_date'] or
                search_term in report['date_range']['end_date'])
        ]
    
    if not filtered_reports:
        st.warning(get_translation(st.session_state.current_language, "no_matching_reports"))
        return
    
    # Display reports
    for i, report in enumerate(filtered_reports):
        with st.expander(f"📄 {report['title']}", expanded=False):
            col1, col2 = st.columns([3, 1])
            
            with col1:
                st.markdown(f"**{get_translation(st.session_state.current_language, 'country')}:** {report['country']['name']}")
                st.markdown(f"**{get_translation(st.session_state.current_language, 'date_range')}:** {report['date_range']['start_date']} to {report['date_range']['end_date']}")
                st.markdown(f"**{get_translation(st.session_state.current_language, 'created')}:** {datetime.fromisoformat(report['created_at']).strftime('%Y-%m-%d %H:%M')}")
                
                # Preview
                st.markdown(f"**{get_translation(st.session_state.current_language, 'preview')}:**")
                st.markdown(f"_{report['report_data']['summary'][:150]}..._")
            
            with col2:
                if st.button(f"👁️ {get_translation(st.session_state.current_language, 'open')}", key=f"open_{i}"):
                    st.session_state.report_data = report['report_data']
                    st.session_state.current_page = 'preview'
                    st.rerun()
                
                if st.button(f"🗑️ {get_translation(st.session_state.current_language, 'delete')}", key=f"delete_{i}"):
                    st.session_state.saved_reports.remove(report)
                    st.rerun()
    
    # Statistics
    st.markdown(f'<h2 class="section-header">📊 {get_translation(st.session_state.current_language, "history_stats")}</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(get_translation(st.session_state.current_language, "total_reports"), len(st.session_state.saved_reports))
    
    with col2:
        unique_countries = len(set(report['country']['code'] for report in st.session_state.saved_reports))
        st.metric(get_translation(st.session_state.current_language, "countries_covered"), unique_countries)
    
    with col3:
        avg_data_points = sum(len(report['report_data']['chart_data']) for report in st.session_state.saved_reports) // len(st.session_state.saved_reports) if st.session_state.saved_reports else 0
        st.metric(get_translation(st.session_state.current_language, "avg_data_points"), avg_data_points)

# Sidebar navigation
with st.sidebar:
    st.markdown(f'<h2 style="color: #1e293b;">🌍 {get_translation(st.session_state.current_language, "app_title")}</h2>', unsafe_allow_html=True)
    
    pages = [
        ("🏠", "nav_home", "home"),
        ("📚", "nav_history", "history"),
        ("⚙️", "nav_settings", "settings"),
        ("❓", "nav_help", "help")
    ]
    
    for icon, name_key, page_key in pages:
        if st.button(f"{icon} {get_translation(st.session_state.current_language, name_key)}", use_container_width=True, key=f"nav_{page_key}"):
            st.session_state.current_page = page_key
            st.rerun()
    
    st.markdown("---")
    st.markdown(f'<p style="color: #6b7280; font-size: 0.875rem;">{get_translation(st.session_state.current_language, "version")}<br>{get_translation(st.session_state.current_language, "built_with")}</p>', unsafe_allow_html=True)

# Main content area
if st.session_state.current_page == 'home':
    render_home_page()
elif st.session_state.current_page == 'preview':
    render_report_preview()
elif st.session_state.current_page == 'help':
    render_help_page()
elif st.session_state.current_page == 'settings':
    render_settings_page()
elif st.session_state.current_page == 'history':
    render_history_page()
