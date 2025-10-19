export interface Translations {
  // Navigation
  home: string;
  help: string;
  settings: string;
  settingsTitle: string;
  history: string;
  
  // Home Screen
  generateReport: string;
  selectCountry: string;
  selectCountryPlaceholder: string;
  startDate: string;
  endDate: string;
  buildReport: string;
  building: string;
  reset: string;
  report: string;
  
  // Progress Steps
  collecting: string;
  processing: string;
  summarizing: string;
  ready: string;
  
  // Report Preview
  reportPreview: string;
  backToHome: string;
  executiveSummary: string;
  keyEvents: string;
  trends: string;
  risks: string;
  dataVisualization: string;
  dataVisualizationDesc: string;
  monthlyTrends: string;
  monthlyComparison: string;
  downloadReport: string;
  downloadPDF: string;
  downloadDOCX: string;
  downloadDescription: string;
  downloading: string;
  mockDownload: string;
  
  // Help Screen
  helpAbout: string;
  howToUse: string;
  step1: string;
  step1Description: string;
  step2: string;
  step2Description: string;
  step3: string;
  step3Description: string;
  features: string;
  comprehensiveReports: string;
  comprehensiveReportsDesc: string;
  multipleFormats: string;
  multipleFormatsDesc: string;
  easyReset: string;
  easyResetDesc: string;
  troubleshooting: string;
  errorCountryDates: string;
  errorCountryDatesDesc: string;
  errorBuildReport: string;
  errorBuildReportDesc: string;
  errorDownload: string;
  errorDownloadDesc: string;
  about: string;
  aboutDescription: string;
  aboutNote: string;
  
  // Settings Screen
  language: string;
  selectLanguage: string;
  saveSettings: string;
  settingsSaved: string;
  
  // History Screen
  reportHistory: string;
  noHistory: string;
  noHistoryDescription: string;
  openReport: string;
  deleteReport: string;
  reportDate: string;
  reportCountry: string;
  clearHistory: string;
  searchReports: string;
  searchPlaceholder: string;
  
  // Common
  loading: string;
  error: string;
  success: string;
  close: string;
  cancel: string;
  confirm: string;
  delete: string;
  save: string;
  back: string;
  next: string;
  previous: string;
}

export const translations: Record<string, Translations> = {
  en: {
    // Navigation
    home: 'Home',
    help: 'Help',
    settings: 'Settings',
    settingsTitle: 'Settings',
    history: 'History',
    
    // Home Screen
    generateReport: 'Generate NGO Report',
    selectCountry: 'Country',
    selectCountryPlaceholder: 'Select a country...',
    startDate: 'Start Date',
    endDate: 'End Date',
    buildReport: 'Build Report',
    building: 'Building...',
    reset: 'Reset',
    report: 'Report',
    
    // Progress Steps
    collecting: 'Collecting Data',
    processing: 'Processing',
    summarizing: 'Summarizing',
    ready: 'Ready',
    
    // Report Preview
    reportPreview: 'Report Preview',
    backToHome: 'Back to Home',
    executiveSummary: 'Executive Summary',
    keyEvents: 'Key Events',
    trends: 'Trends',
    risks: 'Risks',
    dataVisualization: 'Data Visualization',
    dataVisualizationDesc: 'Interactive charts and graphs to better understand trends',
    monthlyTrends: 'Monthly Trends',
    monthlyComparison: 'Monthly Comparison',
    downloadReport: 'Download Report',
    downloadPDF: 'Download PDF',
    downloadDOCX: 'Download DOCX',
    downloadDescription: 'Choose your preferred format to download the complete report.',
    downloading: 'Downloading',
    mockDownload: 'This is a mock download',
    
    // Help Screen
    helpAbout: 'Help & About',
    howToUse: 'How to Use the App',
    step1: 'Step 1: Select Country and Dates',
    step1Description: 'Choose a country from the dropdown menu and select your desired start and end dates for the report period.',
    step2: 'Step 2: Build Report',
    step2Description: 'Click the "Build Report" button to generate your report. You\'ll see progress indicators as the system collects and processes data.',
    step3: 'Step 3: Download Report',
    step3Description: 'Once the report is ready, you can preview it and download it in PDF or DOCX format.',
    features: 'Features',
    comprehensiveReports: 'Comprehensive Reports',
    comprehensiveReportsDesc: 'Get detailed summaries, key events, trends, and risk assessments',
    multipleFormats: 'Multiple Formats',
    multipleFormatsDesc: 'Download reports in PDF or DOCX format for easy sharing',
    easyReset: 'Easy Reset',
    easyResetDesc: 'Clear all inputs and start over with the reset button',
    troubleshooting: 'Troubleshooting',
    errorCountryDates: '"Please pick a country and valid dates"',
    errorCountryDatesDesc: 'Make sure you\'ve selected a country from the dropdown and chosen both start and end dates.',
    errorBuildReport: '"Could not build report"',
    errorBuildReportDesc: 'There was an error processing your request. Try again or check your internet connection.',
    errorDownload: '"Download failed"',
    errorDownloadDesc: 'The download couldn\'t be completed. Try again or check your browser\'s download settings.',
    about: 'About',
    aboutDescription: 'NGO Data Helpers is designed to assist humanitarian organizations and development workers in generating comprehensive reports quickly and efficiently.',
    aboutNote: 'This is a front-end application. Backend integration will be added in future updates.',
    
    // Settings Screen
    language: 'Language',
    selectLanguage: 'Select Language',
    saveSettings: 'Save Settings',
    settingsSaved: 'Settings saved successfully!',
    
    // History Screen
    reportHistory: 'Report History',
    noHistory: 'No Reports Found',
    noHistoryDescription: 'Your generated reports will appear here. Create your first report to get started.',
    openReport: 'Open Report',
    deleteReport: 'Delete',
    reportDate: 'Generated on',
    reportCountry: 'Country',
    clearHistory: 'Clear All History',
    searchReports: 'Search Reports',
    searchPlaceholder: 'Search by country or date...',
    
    // Common
    loading: 'Loading...',
    error: 'Error',
    success: 'Success',
    close: 'Close',
    cancel: 'Cancel',
    confirm: 'Confirm',
    delete: 'Delete',
    save: 'Save',
    back: 'Back',
    next: 'Next',
    previous: 'Previous'
  },
  
  es: {
    // Navigation
    home: 'Inicio',
    help: 'Ayuda',
    settings: 'Configuración',
    settingsTitle: 'Configuración',
    history: 'Historial',
    
    // Home Screen
    generateReport: 'Generar Informe de ONG',
    selectCountry: 'País',
    selectCountryPlaceholder: 'Selecciona un país...',
    startDate: 'Fecha de Inicio',
    endDate: 'Fecha de Fin',
    buildReport: 'Generar Informe',
    building: 'Generando...',
    reset: 'Reiniciar',
    report: 'Informe',
    
    // Progress Steps
    collecting: 'Recopilando Datos',
    processing: 'Procesando',
    summarizing: 'Resumiendo',
    ready: 'Listo',
    
    // Report Preview
    reportPreview: 'Vista Previa del Informe',
    backToHome: 'Volver al Inicio',
    executiveSummary: 'Resumen Ejecutivo',
    keyEvents: 'Eventos Clave',
    trends: 'Tendencias',
    risks: 'Riesgos',
    dataVisualization: 'Visualización de Datos',
    dataVisualizationDesc: 'Gráficos interactivos para entender mejor las tendencias',
    monthlyTrends: 'Tendencias Mensuales',
    monthlyComparison: 'Comparación Mensual',
    downloadReport: 'Descargar Informe',
    downloadPDF: 'Descargar PDF',
    downloadDOCX: 'Descargar DOCX',
    downloadDescription: 'Elige tu formato preferido para descargar el informe completo.',
    downloading: 'Descargando',
    mockDownload: 'Esta es una descarga simulada',
    
    // Help Screen
    helpAbout: 'Ayuda y Acerca de',
    howToUse: 'Cómo Usar la Aplicación',
    step1: 'Paso 1: Seleccionar País y Fechas',
    step1Description: 'Elige un país del menú desplegable y selecciona las fechas de inicio y fin deseadas para el período del informe.',
    step2: 'Paso 2: Generar Informe',
    step2Description: 'Haz clic en el botón "Generar Informe" para crear tu informe. Verás indicadores de progreso mientras el sistema recopila y procesa los datos.',
    step3: 'Paso 3: Descargar Informe',
    step3Description: 'Una vez que el informe esté listo, puedes previsualizarlo y descargarlo en formato PDF o DOCX.',
    features: 'Características',
    comprehensiveReports: 'Informes Integrales',
    comprehensiveReportsDesc: 'Obtén resúmenes detallados, eventos clave, tendencias y evaluaciones de riesgo',
    multipleFormats: 'Múltiples Formatos',
    multipleFormatsDesc: 'Descarga informes en formato PDF o DOCX para compartir fácilmente',
    easyReset: 'Reinicio Fácil',
    easyResetDesc: 'Borra todas las entradas y comienza de nuevo con el botón de reinicio',
    troubleshooting: 'Solución de Problemas',
    errorCountryDates: '"Por favor selecciona un país y fechas válidas"',
    errorCountryDatesDesc: 'Asegúrate de haber seleccionado un país del menú desplegable y elegido tanto la fecha de inicio como la de fin.',
    errorBuildReport: '"No se pudo generar el informe"',
    errorBuildReportDesc: 'Hubo un error procesando tu solicitud. Inténtalo de nuevo o verifica tu conexión a internet.',
    errorDownload: '"Error en la descarga"',
    errorDownloadDesc: 'La descarga no pudo completarse. Inténtalo de nuevo o verifica la configuración de descarga de tu navegador.',
    about: 'Acerca de',
    aboutDescription: 'NGO Data Helpers está diseñado para asistir a organizaciones humanitarias y trabajadores de desarrollo en generar informes integrales de manera rápida y eficiente.',
    aboutNote: 'Esta es una aplicación front-end. La integración con el backend se agregará en futuras actualizaciones.',
    
    // Settings Screen
    language: 'Idioma',
    selectLanguage: 'Seleccionar Idioma',
    saveSettings: 'Guardar Configuración',
    settingsSaved: '¡Configuración guardada exitosamente!',
    
    // History Screen
    reportHistory: 'Historial de Informes',
    noHistory: 'No se Encontraron Informes',
    noHistoryDescription: 'Tus informes generados aparecerán aquí. Crea tu primer informe para comenzar.',
    openReport: 'Abrir Informe',
    deleteReport: 'Eliminar',
    reportDate: 'Generado el',
    reportCountry: 'País',
    clearHistory: 'Limpiar Todo el Historial',
    searchReports: 'Buscar Informes',
    searchPlaceholder: 'Buscar por país o fecha...',
    
    // Common
    loading: 'Cargando...',
    error: 'Error',
    success: 'Éxito',
    close: 'Cerrar',
    cancel: 'Cancelar',
    confirm: 'Confirmar',
    delete: 'Eliminar',
    save: 'Guardar',
    back: 'Atrás',
    next: 'Siguiente',
    previous: 'Anterior'
  },
  
  fr: {
    // Navigation
    home: 'Accueil',
    help: 'Aide',
    settings: 'Paramètres',
    settingsTitle: 'Paramètres',
    history: 'Historique',
    
    // Home Screen
    generateReport: 'Générer un Rapport ONG',
    selectCountry: 'Pays',
    selectCountryPlaceholder: 'Sélectionnez un pays...',
    startDate: 'Date de Début',
    endDate: 'Date de Fin',
    buildReport: 'Générer le Rapport',
    building: 'Génération...',
    reset: 'Réinitialiser',
    report: 'Rapport',
    
    // Progress Steps
    collecting: 'Collecte des Données',
    processing: 'Traitement',
    summarizing: 'Résumé',
    ready: 'Prêt',
    
    // Report Preview
    reportPreview: 'Aperçu du Rapport',
    backToHome: 'Retour à l\'Accueil',
    executiveSummary: 'Résumé Exécutif',
    keyEvents: 'Événements Clés',
    trends: 'Tendances',
    risks: 'Risques',
    dataVisualization: 'Visualisation des Données',
    dataVisualizationDesc: 'Graphiques interactifs pour mieux comprendre les tendances',
    monthlyTrends: 'Tendances Mensuelles',
    monthlyComparison: 'Comparaison Mensuelle',
    downloadReport: 'Télécharger le Rapport',
    downloadPDF: 'Télécharger PDF',
    downloadDOCX: 'Télécharger DOCX',
    downloadDescription: 'Choisissez votre format préféré pour télécharger le rapport complet.',
    downloading: 'Téléchargement',
    mockDownload: 'Ceci est un téléchargement simulé',
    
    // Help Screen
    helpAbout: 'Aide et À Propos',
    howToUse: 'Comment Utiliser l\'Application',
    step1: 'Étape 1: Sélectionner le Pays et les Dates',
    step1Description: 'Choisissez un pays dans le menu déroulant et sélectionnez vos dates de début et de fin souhaitées pour la période du rapport.',
    step2: 'Étape 2: Générer le Rapport',
    step2Description: 'Cliquez sur le bouton "Générer le Rapport" pour créer votre rapport. Vous verrez des indicateurs de progression pendant que le système collecte et traite les données.',
    step3: 'Étape 3: Télécharger le Rapport',
    step3Description: 'Une fois le rapport prêt, vous pouvez le prévisualiser et le télécharger au format PDF ou DOCX.',
    features: 'Fonctionnalités',
    comprehensiveReports: 'Rapports Complets',
    comprehensiveReportsDesc: 'Obtenez des résumés détaillés, des événements clés, des tendances et des évaluations des risques',
    multipleFormats: 'Formats Multiples',
    multipleFormatsDesc: 'Téléchargez les rapports au format PDF ou DOCX pour un partage facile',
    easyReset: 'Réinitialisation Facile',
    easyResetDesc: 'Effacez toutes les entrées et recommencez avec le bouton de réinitialisation',
    troubleshooting: 'Dépannage',
    errorCountryDates: '"Veuillez sélectionner un pays et des dates valides"',
    errorCountryDatesDesc: 'Assurez-vous d\'avoir sélectionné un pays dans le menu déroulant et choisi à la fois la date de début et la date de fin.',
    errorBuildReport: '"Impossible de générer le rapport"',
    errorBuildReportDesc: 'Une erreur s\'est produite lors du traitement de votre demande. Réessayez ou vérifiez votre connexion internet.',
    errorDownload: '"Échec du téléchargement"',
    errorDownloadDesc: 'Le téléchargement n\'a pas pu être terminé. Réessayez ou vérifiez les paramètres de téléchargement de votre navigateur.',
    about: 'À Propos',
    aboutDescription: 'NGO Data Helpers est conçu pour aider les organisations humanitaires et les travailleurs de développement à générer des rapports complets rapidement et efficacement.',
    aboutNote: 'Il s\'agit d\'une application front-end. L\'intégration backend sera ajoutée dans les futures mises à jour.',
    
    // Settings Screen
    language: 'Langue',
    selectLanguage: 'Sélectionner la Langue',
    saveSettings: 'Enregistrer les Paramètres',
    settingsSaved: 'Paramètres enregistrés avec succès !',
    
    // History Screen
    reportHistory: 'Historique des Rapports',
    noHistory: 'Aucun Rapport Trouvé',
    noHistoryDescription: 'Vos rapports générés apparaîtront ici. Créez votre premier rapport pour commencer.',
    openReport: 'Ouvrir le Rapport',
    deleteReport: 'Supprimer',
    reportDate: 'Généré le',
    reportCountry: 'Pays',
    clearHistory: 'Effacer Tout l\'Historique',
    searchReports: 'Rechercher des Rapports',
    searchPlaceholder: 'Rechercher par pays ou date...',
    
    // Common
    loading: 'Chargement...',
    error: 'Erreur',
    success: 'Succès',
    close: 'Fermer',
    cancel: 'Annuler',
    confirm: 'Confirmer',
    delete: 'Supprimer',
    save: 'Enregistrer',
    back: 'Retour',
    next: 'Suivant',
    previous: 'Précédent'
  },
  
  ar: {
    // Navigation
    home: 'الرئيسية',
    help: 'المساعدة',
    settings: 'الإعدادات',
    settingsTitle: 'الإعدادات',
    history: 'السجل',
    
    // Home Screen
    generateReport: 'إنشاء تقرير المنظمات غير الحكومية',
    selectCountry: 'البلد',
    selectCountryPlaceholder: 'اختر بلداً...',
    startDate: 'تاريخ البداية',
    endDate: 'تاريخ النهاية',
    buildReport: 'إنشاء التقرير',
    building: 'جاري الإنشاء...',
    reset: 'إعادة تعيين',
    report: 'التقرير',
    
    // Progress Steps
    collecting: 'جمع البيانات',
    processing: 'المعالجة',
    summarizing: 'التلخيص',
    ready: 'جاهز',
    
    // Report Preview
    reportPreview: 'معاينة التقرير',
    backToHome: 'العودة للرئيسية',
    executiveSummary: 'الملخص التنفيذي',
    keyEvents: 'الأحداث الرئيسية',
    trends: 'الاتجاهات',
    risks: 'المخاطر',
    dataVisualization: 'تصور البيانات',
    dataVisualizationDesc: 'رسوم بيانية تفاعلية لفهم الاتجاهات بشكل أفضل',
    monthlyTrends: 'الاتجاهات الشهرية',
    monthlyComparison: 'المقارنة الشهرية',
    downloadReport: 'تحميل التقرير',
    downloadPDF: 'تحميل PDF',
    downloadDOCX: 'تحميل DOCX',
    downloadDescription: 'اختر التنسيق المفضل لديك لتحميل التقرير الكامل.',
    downloading: 'جاري التحميل',
    mockDownload: 'هذا تحميل وهمي',
    
    // Help Screen
    helpAbout: 'المساعدة وحول',
    howToUse: 'كيفية استخدام التطبيق',
    step1: 'الخطوة 1: اختيار البلد والتواريخ',
    step1Description: 'اختر بلداً من القائمة المنسدلة وحدد تواريخ البداية والنهاية المطلوبة لفترة التقرير.',
    step2: 'الخطوة 2: إنشاء التقرير',
    step2Description: 'انقر على زر "إنشاء التقرير" لتوليد تقريرك. سترى مؤشرات التقدم بينما يجمع النظام ويعالج البيانات.',
    step3: 'الخطوة 3: تحميل التقرير',
    step3Description: 'بمجرد أن يصبح التقرير جاهزاً، يمكنك معاينته وتحميله بتنسيق PDF أو DOCX.',
    features: 'الميزات',
    comprehensiveReports: 'التقارير الشاملة',
    comprehensiveReportsDesc: 'احصل على ملخصات مفصلة وأحداث رئيسية واتجاهات وتقييمات للمخاطر',
    multipleFormats: 'تنسيقات متعددة',
    multipleFormatsDesc: 'قم بتحميل التقارير بتنسيق PDF أو DOCX للمشاركة السهلة',
    easyReset: 'إعادة تعيين سهلة',
    easyResetDesc: 'امسح جميع المدخلات وابدأ من جديد بزر إعادة التعيين',
    troubleshooting: 'استكشاف الأخطاء وإصلاحها',
    errorCountryDates: '"يرجى اختيار بلد وتواريخ صحيحة"',
    errorCountryDatesDesc: 'تأكد من اختيار بلد من القائمة المنسدلة واختيار كل من تاريخ البداية وتاريخ النهاية.',
    errorBuildReport: '"لا يمكن إنشاء التقرير"',
    errorBuildReportDesc: 'حدث خطأ في معالجة طلبك. حاول مرة أخرى أو تحقق من اتصالك بالإنترنت.',
    errorDownload: '"فشل التحميل"',
    errorDownloadDesc: 'لا يمكن إكمال التحميل. حاول مرة أخرى أو تحقق من إعدادات التحميل في متصفحك.',
    about: 'حول',
    aboutDescription: 'مساعد بيانات المنظمات غير الحكومية مصمم لمساعدة المنظمات الإنسانية وعمال التنمية في إنشاء تقارير شاملة بسرعة وكفاءة.',
    aboutNote: 'هذا تطبيق واجهة أمامية. سيتم إضافة التكامل مع الخادم في التحديثات المستقبلية.',
    
    // Settings Screen
    language: 'اللغة',
    selectLanguage: 'اختر اللغة',
    saveSettings: 'حفظ الإعدادات',
    settingsSaved: 'تم حفظ الإعدادات بنجاح!',
    
    // History Screen
    reportHistory: 'سجل التقارير',
    noHistory: 'لم يتم العثور على تقارير',
    noHistoryDescription: 'ستظهر تقاريرك المُنشأة هنا. أنشئ تقريرك الأول للبدء.',
    openReport: 'فتح التقرير',
    deleteReport: 'حذف',
    reportDate: 'تم الإنشاء في',
    reportCountry: 'البلد',
    clearHistory: 'مسح كامل السجل',
    searchReports: 'البحث في التقارير',
    searchPlaceholder: 'البحث بالبلد أو التاريخ...',
    
    // Common
    loading: 'جاري التحميل...',
    error: 'خطأ',
    success: 'نجح',
    close: 'إغلاق',
    cancel: 'إلغاء',
    confirm: 'تأكيد',
    delete: 'حذف',
    save: 'حفظ',
    back: 'رجوع',
    next: 'التالي',
    previous: 'السابق'
  }
};

export const supportedLanguages = [
  { code: 'en', name: 'English', flag: '🇺🇸' },
  { code: 'es', name: 'Español', flag: '🇪🇸' },
  { code: 'fr', name: 'Français', flag: '🇫🇷' },
  { code: 'ar', name: 'العربية', flag: '🇸🇦' }
];

export const getTranslation = (language: string, key: keyof Translations): string => {
  const lang = translations[language] || translations.en;
  return lang[key] || translations.en[key];
};