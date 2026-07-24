import { Routes, Route, Navigate } from "react-router-dom";

import MainLayout from "@/layouts/MainLayout";

// Landing
import LandingPage from "@/pages/landing/LandingPage";

// Authentication
import LoginPage from "@/pages/auth/LoginPage";
import RegisterPage from "@/pages/auth/RegisterPage";

// Dashboard
import DashboardPage from "@/pages/dashboard/DashboardPage";

// Assessment
import AssessmentPage from "@/pages/assessment/AssessmentPage";

// Chatbot
import ChatbotPage from "@/pages/chatbot/ChatbotPage";

// Recommendation
import RecommendationPage from "@/pages/recommendation/RecommendationPage";

// History
import HistoryPage from "@/pages/history/HistoryPage";

// Emergency
import EmergencyPage from "@/pages/emergency/EmergencyPage";

// Profile
import ProfilePage from "@/pages/profile/ProfilePage";

// Settings
import SettingsPage from "@/pages/settings/SettingsPage";

export default function AppRoutes() {
  return (
    <Routes>

      {/* Landing Page */}

      <Route
        path="/"
        element={<LandingPage />}
      />

      {/* Authentication */}

      <Route
        path="/login"
        element={<LoginPage />}
      />

      <Route
        path="/register"
        element={<RegisterPage />}
      />

      {/* Dashboard Layout */}

      <Route element={<MainLayout />}>

        <Route
          path="/dashboard"
          element={<DashboardPage />}
        />

        <Route
          path="/assessment"
          element={<AssessmentPage />}
        />

        <Route
          path="/chatbot"
          element={<ChatbotPage />}
        />

        <Route
          path="/recommendations"
          element={<RecommendationPage />}
        />

        <Route
          path="/history"
          element={<HistoryPage />}
        />

        <Route
          path="/emergency"
          element={<EmergencyPage />}
        />

        <Route
          path="/profile"
          element={<ProfilePage />}
        />

        <Route
          path="/settings"
          element={<SettingsPage />}
        />

      </Route>

      {/* 404 */}

      <Route
        path="*"
        element={<Navigate to="/" replace />}
      />

    </Routes>
  );
}