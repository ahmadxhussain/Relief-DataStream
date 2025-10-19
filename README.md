# NGO Data Helpers - Front End

A React-based front-end application for NGO data helpers to generate comprehensive humanitarian and development reports.

## Features

- **Country Selection**: Choose from 195+ countries
- **Date Range Selection**: Pick custom start and end dates
- **Progress Tracking**: Real-time progress indicators during report generation
- **Report Preview**: Comprehensive reports with summaries, key events, trends, and risks
- **Data Visualization**: Interactive charts and graphs using Recharts
- **Download Options**: Export reports in PDF or DOCX format
- **Error Handling**: Clear error messages and user guidance
- **Responsive Design**: Works on desktop and mobile devices

## Getting Started

### Prerequisites

- Node.js (v16 or higher)
- npm or yarn

### Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm run dev
   ```

4. Open your browser and navigate to `http://localhost:5174`

### Building for Production

```bash
npm run build
```

## Usage

1. **Select Country and Dates**: Choose a country from the dropdown and select your desired date range
2. **Build Report**: Click the "Build Report" button to generate your report
3. **Monitor Progress**: Watch the progress indicators as the system processes your request
4. **Preview Report**: Review the generated report with summaries, events, trends, and charts
5. **Download**: Choose your preferred format (PDF or DOCX) and download the report

## Technology Stack

- **React 18** with TypeScript
- **Vite** for fast development and building
- **Recharts** for data visualization
- **Lucide React** for icons
- **CSS3** for styling with modern design principles

## Project Structure

```
src/
├── components/          # React components
│   ├── Header.tsx      # Navigation header
│   ├── HomeScreen.tsx  # Main report builder screen
│   ├── ReportPreview.tsx # Report display screen
│   ├── HelpScreen.tsx  # Help and about screen
│   └── ErrorBanner.tsx # Error display component
├── data/               # Mock data and utilities
│   └── mockData.ts     # Country list and mock report data
├── types.ts            # TypeScript type definitions
├── App.tsx             # Main application component
├── main.tsx            # Application entry point
└── index.css           # Global styles
```

## Future Enhancements

- Backend integration for real data
- Language selection (stretch goal)
- Report history and saved reports (stretch goal)
- Advanced filtering and search options
- User authentication and accounts
- Real-time data updates

## Development

This is a front-end only application. Backend integration will be added in future updates to connect with real data sources and provide actual report generation capabilities.

## License

This project is part of the UTD Fall Project 2025 Capstone.
