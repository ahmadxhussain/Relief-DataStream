# Translation system for NGO Data Helpers
# Supports English, Spanish, French, and Arabic

TRANSLATIONS = {
    'en': {
        # Navigation
        'nav_home': 'Home',
        'nav_history': 'History', 
        'nav_settings': 'Settings',
        'nav_help': 'Help',
        
        # Main headers
        'app_title': 'NGO Data Helpers',
        'app_subtitle': 'Generate comprehensive humanitarian and development reports for any country',
        'report_preview': 'Report Preview',
        'help_title': 'Help & About',
        'settings_title': 'Settings',
        'history_title': 'Report History',
        
        # Home page
        'select_country': 'Select Country',
        'select_country_placeholder': 'Choose a country...',
        'select_date_range': 'Select Date Range',
        'start_date': 'Start Date',
        'end_date': 'End Date',
        'build_report': 'Build Report',
        'building': 'Building...',
        'reset': 'Reset',
        'progress_title': 'Progress',
        
        # Progress steps
        'step_collecting': 'Collecting Data',
        'step_processing': 'Processing',
        'step_summarizing': 'Summarizing',
        'step_ready': 'Ready',
        
        # Report sections
        'executive_summary': 'Executive Summary',
        'key_events': 'Key Events',
        'trends': 'Trends',
        'risks': 'Risks',
        'data_visualization': 'Data Visualization',
        'monthly_trends': 'Monthly Trends',
        'monthly_comparison': 'Monthly Comparison',
        'download_report': 'Download Report',
        'download_description': 'Download your report in your preferred format:',
        'download_pdf': 'Download PDF',
        'download_docx': 'Download DOCX',
        'back_to_home': 'Back to Home',
        
        # Help page
        'how_to_use': 'How to Use the App',
        'help_description': 'The NGO Data Helpers app allows you to generate comprehensive humanitarian and development reports for any country within a specified date range.',
        'step1_title': 'Select Country and Dates',
        'step1_desc': 'Choose a country from the dropdown menu and select your desired start and end dates for the report period.',
        'step2_title': 'Build Report',
        'step2_desc': 'Click the "Build Report" button to generate your report. You\'ll see progress indicators as the system processes your request.',
        'step3_title': 'Preview Report',
        'step3_desc': 'Review the generated report with summaries, events, trends, and interactive charts.',
        'step4_title': 'Download Report',
        'step4_desc': 'Once the report is ready, you can preview it and download it in PDF or DOCX format.',
        'features_title': 'Features',
        'feature_reports': 'Comprehensive Reports',
        'feature_reports_desc': 'Get detailed summaries, key events, trends, and risk assessments',
        'feature_charts': 'Data Visualization',
        'feature_charts_desc': 'Interactive charts and graphs to better understand trends',
        'feature_download': 'Multiple Formats',
        'feature_download_desc': 'Download reports in PDF or DOCX format for easy sharing',
        'feature_reset': 'Easy Reset',
        'feature_reset_desc': 'Clear all inputs and start over with the reset button',
        'troubleshooting_title': 'Troubleshooting',
        'error_country_dates': 'Please pick a country and valid dates',
        'error_country_dates_desc': 'Make sure you\'ve selected a country from the dropdown and chosen both start and end dates.',
        'error_build_report': 'Could not build report',
        'error_build_report_desc': 'There was an error processing your request. Try again or check your internet connection.',
        'error_download': 'Download failed',
        'error_download_desc': 'The download couldn\'t be completed. Try again or check your browser\'s download settings.',
        'about_title': 'About',
        'about_desc': 'NGO Data Helpers is designed to assist humanitarian organizations and development workers in generating comprehensive reports quickly and efficiently.',
        'about_note': 'This is a front-end application. Backend integration will be added in future updates.',
        
        # Settings page
        'language_settings': 'Language Settings',
        'select_language': 'Select Language:',
        'save_settings': 'Save Settings',
        'settings_saved': 'Settings saved successfully!',
        'language_info': 'Language Information',
        'language_info_desc': 'Complete translation for all interface elements',
        'settings_persistence': 'Settings Persistence',
        'settings_persistence_desc': 'Your language preference is automatically saved and will be remembered the next time you visit the application.',
        'theme_settings': 'Theme Settings',
        'select_theme': 'Select Theme:',
        'light_mode': 'Light Mode',
        'dark_mode': 'Dark Mode',
        'theme_info': 'Theme Information',
        'theme_info_desc': 'Choose your preferred color scheme for the interface',
        
        # History page
        'no_reports': 'No reports found',
        'no_reports_desc': 'Generate your first report to see it here!',
        'search_reports': 'Search reports:',
        'search_placeholder': 'Search by country, date, or title...',
        'no_matching_reports': 'No reports match your search criteria.',
        'country': 'Country',
        'date_range': 'Date Range',
        'created': 'Created',
        'preview': 'Preview',
        'open': 'Open',
        'delete': 'Delete',
        'history_stats': 'History Statistics',
        'total_reports': 'Total Reports',
        'countries_covered': 'Countries Covered',
        'avg_data_points': 'Avg Data Points',
        
        # Common
        'dismiss': 'Dismiss',
        'back': 'Back',
        'version': 'Version 1.0.0',
        'built_with': 'Built with Streamlit'
    },
    
    'es': {
        # Navigation
        'nav_home': 'Inicio',
        'nav_history': 'Historial', 
        'nav_settings': 'Configuración',
        'nav_help': 'Ayuda',
        
        # Main headers
        'app_title': 'Ayudantes de Datos ONG',
        'app_subtitle': 'Genera informes integrales humanitarios y de desarrollo para cualquier país',
        'report_preview': 'Vista Previa del Informe',
        'help_title': 'Ayuda y Acerca de',
        'settings_title': 'Configuración',
        'history_title': 'Historial de Informes',
        
        # Home page
        'select_country': 'Seleccionar País',
        'select_country_placeholder': 'Elige un país...',
        'select_date_range': 'Seleccionar Rango de Fechas',
        'start_date': 'Fecha de Inicio',
        'end_date': 'Fecha de Fin',
        'build_report': 'Generar Informe',
        'building': 'Generando...',
        'reset': 'Restablecer',
        'progress_title': 'Progreso',
        
        # Progress steps
        'step_collecting': 'Recopilando Datos',
        'step_processing': 'Procesando',
        'step_summarizing': 'Resumiendo',
        'step_ready': 'Listo',
        
        # Report sections
        'executive_summary': 'Resumen Ejecutivo',
        'key_events': 'Eventos Clave',
        'trends': 'Tendencias',
        'risks': 'Riesgos',
        'data_visualization': 'Visualización de Datos',
        'monthly_trends': 'Tendencias Mensuales',
        'monthly_comparison': 'Comparación Mensual',
        'download_report': 'Descargar Informe',
        'download_description': 'Descarga tu informe en tu formato preferido:',
        'download_pdf': 'Descargar PDF',
        'download_docx': 'Descargar DOCX',
        'back_to_home': 'Volver al Inicio',
        
        # Help page
        'how_to_use': 'Cómo Usar la Aplicación',
        'help_description': 'La aplicación Ayudantes de Datos ONG te permite generar informes integrales humanitarios y de desarrollo para cualquier país dentro de un rango de fechas específico.',
        'step1_title': 'Seleccionar País y Fechas',
        'step1_desc': 'Elige un país del menú desplegable y selecciona las fechas de inicio y fin deseadas para el período del informe.',
        'step2_title': 'Generar Informe',
        'step2_desc': 'Haz clic en el botón "Generar Informe" para crear tu informe. Verás indicadores de progreso mientras el sistema procesa tu solicitud.',
        'step3_title': 'Vista Previa del Informe',
        'step3_desc': 'Revisa el informe generado con resúmenes, eventos, tendencias y gráficos interactivos.',
        'step4_title': 'Descargar Informe',
        'step4_desc': 'Una vez que el informe esté listo, puedes previsualizarlo y descargarlo en formato PDF o DOCX.',
        'features_title': 'Características',
        'feature_reports': 'Informes Integrales',
        'feature_reports_desc': 'Obtén resúmenes detallados, eventos clave, tendencias y evaluaciones de riesgo',
        'feature_charts': 'Visualización de Datos',
        'feature_charts_desc': 'Gráficos y tablas interactivas para entender mejor las tendencias',
        'feature_download': 'Múltiples Formatos',
        'feature_download_desc': 'Descarga informes en formato PDF o DOCX para compartir fácilmente',
        'feature_reset': 'Restablecimiento Fácil',
        'feature_reset_desc': 'Borra todas las entradas y comienza de nuevo con el botón de restablecer',
        'troubleshooting_title': 'Solución de Problemas',
        'error_country_dates': 'Por favor selecciona un país y fechas válidas',
        'error_country_dates_desc': 'Asegúrate de haber seleccionado un país del menú desplegable y haber elegido tanto la fecha de inicio como la de fin.',
        'error_build_report': 'No se pudo generar el informe',
        'error_build_report_desc': 'Hubo un error procesando tu solicitud. Inténtalo de nuevo o verifica tu conexión a internet.',
        'error_download': 'Descarga fallida',
        'error_download_desc': 'La descarga no pudo completarse. Inténtalo de nuevo o verifica la configuración de descarga de tu navegador.',
        'about_title': 'Acerca de',
        'about_desc': 'Ayudantes de Datos ONG está diseñado para asistir a organizaciones humanitarias y trabajadores de desarrollo en generar informes integrales de manera rápida y eficiente.',
        'about_note': 'Esta es una aplicación de front-end. La integración del backend se agregará en actualizaciones futuras.',
        
        # Settings page
        'language_settings': 'Configuración de Idioma',
        'select_language': 'Seleccionar Idioma:',
        'save_settings': 'Guardar Configuración',
        'settings_saved': '¡Configuración guardada exitosamente!',
        'language_info': 'Información del Idioma',
        'language_info_desc': 'Traducción completa para todos los elementos de la interfaz',
        'settings_persistence': 'Persistencia de Configuración',
        'settings_persistence_desc': 'Tu preferencia de idioma se guarda automáticamente y será recordada la próxima vez que visites la aplicación.',
        'theme_settings': 'Configuración de Tema',
        'select_theme': 'Seleccionar Tema:',
        'light_mode': 'Modo Claro',
        'dark_mode': 'Modo Oscuro',
        'theme_info': 'Información del Tema',
        'theme_info_desc': 'Elige tu esquema de colores preferido para la interfaz',
        
        # History page
        'no_reports': 'No se encontraron informes',
        'no_reports_desc': '¡Genera tu primer informe para verlo aquí!',
        'search_reports': 'Buscar informes:',
        'search_placeholder': 'Buscar por país, fecha o título...',
        'no_matching_reports': 'Ningún informe coincide con tus criterios de búsqueda.',
        'country': 'País',
        'date_range': 'Rango de Fechas',
        'created': 'Creado',
        'preview': 'Vista Previa',
        'open': 'Abrir',
        'delete': 'Eliminar',
        'history_stats': 'Estadísticas del Historial',
        'total_reports': 'Total de Informes',
        'countries_covered': 'Países Cubiertos',
        'avg_data_points': 'Puntos de Datos Promedio',
        
        # Common
        'dismiss': 'Descartar',
        'back': 'Atrás',
        'version': 'Versión 1.0.0',
        'built_with': 'Construido con Streamlit'
    },
    
    'fr': {
        # Navigation
        'nav_home': 'Accueil',
        'nav_history': 'Historique', 
        'nav_settings': 'Paramètres',
        'nav_help': 'Aide',
        
        # Main headers
        'app_title': 'Aides aux Données ONG',
        'app_subtitle': 'Générez des rapports complets humanitaires et de développement pour n\'importe quel pays',
        'report_preview': 'Aperçu du Rapport',
        'help_title': 'Aide et À Propos',
        'settings_title': 'Paramètres',
        'history_title': 'Historique des Rapports',
        
        # Home page
        'select_country': 'Sélectionner un Pays',
        'select_country_placeholder': 'Choisissez un pays...',
        'select_date_range': 'Sélectionner la Plage de Dates',
        'start_date': 'Date de Début',
        'end_date': 'Date de Fin',
        'build_report': 'Générer le Rapport',
        'building': 'Génération...',
        'reset': 'Réinitialiser',
        'progress_title': 'Progrès',
        
        # Progress steps
        'step_collecting': 'Collecte de Données',
        'step_processing': 'Traitement',
        'step_summarizing': 'Résumé',
        'step_ready': 'Prêt',
        
        # Report sections
        'executive_summary': 'Résumé Exécutif',
        'key_events': 'Événements Clés',
        'trends': 'Tendances',
        'risks': 'Risques',
        'data_visualization': 'Visualisation des Données',
        'monthly_trends': 'Tendances Mensuelles',
        'monthly_comparison': 'Comparaison Mensuelle',
        'download_report': 'Télécharger le Rapport',
        'download_description': 'Téléchargez votre rapport dans votre format préféré :',
        'download_pdf': 'Télécharger PDF',
        'download_docx': 'Télécharger DOCX',
        'back_to_home': 'Retour à l\'Accueil',
        
        # Help page
        'how_to_use': 'Comment Utiliser l\'Application',
        'help_description': 'L\'application Aides aux Données ONG vous permet de générer des rapports complets humanitaires et de développement pour n\'importe quel pays dans une plage de dates spécifique.',
        'step1_title': 'Sélectionner le Pays et les Dates',
        'step1_desc': 'Choisissez un pays dans le menu déroulant et sélectionnez vos dates de début et de fin souhaitées pour la période du rapport.',
        'step2_title': 'Générer le Rapport',
        'step2_desc': 'Cliquez sur le bouton "Générer le Rapport" pour créer votre rapport. Vous verrez des indicateurs de progression pendant que le système traite votre demande.',
        'step3_title': 'Aperçu du Rapport',
        'step3_desc': 'Examinez le rapport généré avec des résumés, des événements, des tendances et des graphiques interactifs.',
        'step4_title': 'Télécharger le Rapport',
        'step4_desc': 'Une fois le rapport prêt, vous pouvez le prévisualiser et le télécharger au format PDF ou DOCX.',
        'features_title': 'Caractéristiques',
        'feature_reports': 'Rapports Complets',
        'feature_reports_desc': 'Obtenez des résumés détaillés, des événements clés, des tendances et des évaluations des risques',
        'feature_charts': 'Visualisation des Données',
        'feature_charts_desc': 'Graphiques et tableaux interactifs pour mieux comprendre les tendances',
        'feature_download': 'Formats Multiples',
        'feature_download_desc': 'Téléchargez les rapports au format PDF ou DOCX pour un partage facile',
        'feature_reset': 'Réinitialisation Facile',
        'feature_reset_desc': 'Effacez toutes les entrées et recommencez avec le bouton de réinitialisation',
        'troubleshooting_title': 'Dépannage',
        'error_country_dates': 'Veuillez sélectionner un pays et des dates valides',
        'error_country_dates_desc': 'Assurez-vous d\'avoir sélectionné un pays dans le menu déroulant et choisi à la fois les dates de début et de fin.',
        'error_build_report': 'Impossible de générer le rapport',
        'error_build_report_desc': 'Il y a eu une erreur lors du traitement de votre demande. Réessayez ou vérifiez votre connexion internet.',
        'error_download': 'Échec du téléchargement',
        'error_download_desc': 'Le téléchargement n\'a pas pu être complété. Réessayez ou vérifiez les paramètres de téléchargement de votre navigateur.',
        'about_title': 'À Propos',
        'about_desc': 'Aides aux Données ONG est conçu pour aider les organisations humanitaires et les travailleurs du développement à générer des rapports complets rapidement et efficacement.',
        'about_note': 'Ceci est une application front-end. L\'intégration du backend sera ajoutée dans les futures mises à jour.',
        
        # Settings page
        'language_settings': 'Paramètres de Langue',
        'select_language': 'Sélectionner la Langue :',
        'save_settings': 'Enregistrer les Paramètres',
        'settings_saved': 'Paramètres enregistrés avec succès !',
        'language_info': 'Informations sur la Langue',
        'language_info_desc': 'Traduction complète pour tous les éléments de l\'interface',
        'settings_persistence': 'Persistance des Paramètres',
        'settings_persistence_desc': 'Votre préférence de langue est automatiquement sauvegardée et sera mémorisée la prochaine fois que vous visiterez l\'application.',
        'theme_settings': 'Paramètres de Thème',
        'select_theme': 'Sélectionner le Thème :',
        'light_mode': 'Mode Clair',
        'dark_mode': 'Mode Sombre',
        'theme_info': 'Informations sur le Thème',
        'theme_info_desc': 'Choisissez votre schéma de couleurs préféré pour l\'interface',
        
        # History page
        'no_reports': 'Aucun rapport trouvé',
        'no_reports_desc': 'Générez votre premier rapport pour le voir ici !',
        'search_reports': 'Rechercher des rapports :',
        'search_placeholder': 'Rechercher par pays, date ou titre...',
        'no_matching_reports': 'Aucun rapport ne correspond à vos critères de recherche.',
        'country': 'Pays',
        'date_range': 'Plage de Dates',
        'created': 'Créé',
        'preview': 'Aperçu',
        'open': 'Ouvrir',
        'delete': 'Supprimer',
        'history_stats': 'Statistiques de l\'Historique',
        'total_reports': 'Total des Rapports',
        'countries_covered': 'Pays Couverts',
        'avg_data_points': 'Points de Données Moyens',
        
        # Common
        'dismiss': 'Rejeter',
        'back': 'Retour',
        'version': 'Version 1.0.0',
        'built_with': 'Construit avec Streamlit'
    },
    
    'ar': {
        # Navigation
        'nav_home': 'الرئيسية',
        'nav_history': 'التاريخ', 
        'nav_settings': 'الإعدادات',
        'nav_help': 'المساعدة',
        
        # Main headers
        'app_title': 'مساعدو بيانات المنظمات غير الحكومية',
        'app_subtitle': 'قم بتوليد تقارير إنسانية وتنموية شاملة لأي بلد',
        'report_preview': 'معاينة التقرير',
        'help_title': 'المساعدة وحول',
        'settings_title': 'الإعدادات',
        'history_title': 'تاريخ التقارير',
        
        # Home page
        'select_country': 'اختر البلد',
        'select_country_placeholder': 'اختر بلداً...',
        'select_date_range': 'اختر نطاق التاريخ',
        'start_date': 'تاريخ البداية',
        'end_date': 'تاريخ النهاية',
        'build_report': 'إنشاء التقرير',
        'building': 'جاري الإنشاء...',
        'reset': 'إعادة تعيين',
        'progress_title': 'التقدم',
        
        # Progress steps
        'step_collecting': 'جمع البيانات',
        'step_processing': 'المعالجة',
        'step_summarizing': 'التلخيص',
        'step_ready': 'جاهز',
        
        # Report sections
        'executive_summary': 'الملخص التنفيذي',
        'key_events': 'الأحداث الرئيسية',
        'trends': 'الاتجاهات',
        'risks': 'المخاطر',
        'data_visualization': 'تصور البيانات',
        'monthly_trends': 'الاتجاهات الشهرية',
        'monthly_comparison': 'المقارنة الشهرية',
        'download_report': 'تحميل التقرير',
        'download_description': 'قم بتحميل تقريرك بالتنسيق المفضل لديك:',
        'download_pdf': 'تحميل PDF',
        'download_docx': 'تحميل DOCX',
        'back_to_home': 'العودة للرئيسية',
        
        # Help page
        'how_to_use': 'كيفية استخدام التطبيق',
        'help_description': 'يتيح تطبيق مساعدو بيانات المنظمات غير الحكومية توليد تقارير إنسانية وتنموية شاملة لأي بلد ضمن نطاق تاريخ محدد.',
        'step1_title': 'اختر البلد والتواريخ',
        'step1_desc': 'اختر بلداً من القائمة المنسدلة وحدد تواريخ البداية والنهاية المطلوبة لفترة التقرير.',
        'step2_title': 'إنشاء التقرير',
        'step2_desc': 'انقر على زر "إنشاء التقرير" لتوليد تقريرك. سترى مؤشرات التقدم بينما يعالج النظام طلبك.',
        'step3_title': 'معاينة التقرير',
        'step3_desc': 'راجع التقرير المُولد مع الملخصات والأحداث والاتجاهات والرسوم البيانية التفاعلية.',
        'step4_title': 'تحميل التقرير',
        'step4_desc': 'بمجرد أن يصبح التقرير جاهزاً، يمكنك معاينته وتحميله بتنسيق PDF أو DOCX.',
        'features_title': 'الميزات',
        'feature_reports': 'التقارير الشاملة',
        'feature_reports_desc': 'احصل على ملخصات مفصلة وأحداث رئيسية واتجاهات وتقييمات للمخاطر',
        'feature_charts': 'تصور البيانات',
        'feature_charts_desc': 'رسوم بيانية وجداول تفاعلية لفهم الاتجاهات بشكل أفضل',
        'feature_download': 'تنسيقات متعددة',
        'feature_download_desc': 'قم بتحميل التقارير بتنسيق PDF أو DOCX للمشاركة السهلة',
        'feature_reset': 'إعادة تعيين سهلة',
        'feature_reset_desc': 'امسح جميع المدخلات وابدأ من جديد باستخدام زر إعادة التعيين',
        'troubleshooting_title': 'استكشاف الأخطاء',
        'error_country_dates': 'يرجى اختيار بلد وتواريخ صحيحة',
        'error_country_dates_desc': 'تأكد من اختيار بلد من القائمة المنسدلة واختيار كل من تاريخ البداية والنهاية.',
        'error_build_report': 'لا يمكن إنشاء التقرير',
        'error_build_report_desc': 'حدث خطأ في معالجة طلبك. حاول مرة أخرى أو تحقق من اتصالك بالإنترنت.',
        'error_download': 'فشل التحميل',
        'error_download_desc': 'لا يمكن إكمال التحميل. حاول مرة أخرى أو تحقق من إعدادات التحميل في متصفحك.',
        'about_title': 'حول',
        'about_desc': 'تم تصميم مساعدو بيانات المنظمات غير الحكومية لمساعدة المنظمات الإنسانية والعاملين في التنمية على توليد تقارير شاملة بسرعة وكفاءة.',
        'about_note': 'هذا تطبيق واجهة أمامية. سيتم إضافة تكامل الخادم الخلفي في التحديثات المستقبلية.',
        
        # Settings page
        'language_settings': 'إعدادات اللغة',
        'select_language': 'اختر اللغة:',
        'save_settings': 'حفظ الإعدادات',
        'settings_saved': 'تم حفظ الإعدادات بنجاح!',
        'language_info': 'معلومات اللغة',
        'language_info_desc': 'ترجمة كاملة لجميع عناصر الواجهة',
        'settings_persistence': 'استمرارية الإعدادات',
        'settings_persistence_desc': 'يتم حفظ تفضيل اللغة تلقائياً وسيتم تذكره في المرة القادمة التي تزور فيها التطبيق.',
        'theme_settings': 'إعدادات المظهر',
        'select_theme': 'اختر المظهر:',
        'light_mode': 'الوضع الفاتح',
        'dark_mode': 'الوضع المظلم',
        'theme_info': 'معلومات المظهر',
        'theme_info_desc': 'اختر نظام الألوان المفضل لديك للواجهة',
        
        # History page
        'no_reports': 'لم يتم العثور على تقارير',
        'no_reports_desc': 'قم بإنشاء تقريرك الأول لتراه هنا!',
        'search_reports': 'البحث في التقارير:',
        'search_placeholder': 'البحث بالبلد أو التاريخ أو العنوان...',
        'no_matching_reports': 'لا توجد تقارير تطابق معايير البحث الخاصة بك.',
        'country': 'البلد',
        'date_range': 'نطاق التاريخ',
        'created': 'تم الإنشاء',
        'preview': 'معاينة',
        'open': 'فتح',
        'delete': 'حذف',
        'history_stats': 'إحصائيات التاريخ',
        'total_reports': 'إجمالي التقارير',
        'countries_covered': 'البلدان المغطاة',
        'avg_data_points': 'متوسط نقاط البيانات',
        
        # Common
        'dismiss': 'رفض',
        'back': 'رجوع',
        'version': 'الإصدار 1.0.0',
        'built_with': 'مبني بـ Streamlit'
    }
}

def get_translation(language: str, key: str) -> str:
    """Get translation for a given language and key"""
    if language not in TRANSLATIONS:
        language = 'en'  # Fallback to English
    
    if key not in TRANSLATIONS[language]:
        # Fallback to English if key not found
        return TRANSLATIONS['en'].get(key, key)
    
    return TRANSLATIONS[language][key]

def get_supported_languages():
    """Get list of supported languages"""
    return [
        {'code': 'en', 'name': 'English', 'flag': '🇺🇸'},
        {'code': 'es', 'name': 'Spanish', 'flag': '🇪🇸'},
        {'code': 'fr', 'name': 'French', 'flag': '🇫🇷'},
        {'code': 'ar', 'name': 'Arabic', 'flag': '🇸🇦'}
    ]
