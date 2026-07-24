import { NavLink } from "react-router-dom";
import {
  LayoutDashboard,
  ClipboardCheck,
  MessageSquareHeart,
  Lightbulb,
  History,
  Siren,
  User,
  Settings,
  Brain,
} from "lucide-react";

const menuItems = [
  {
    title: "Dashboard",
    path: "/dashboard",
    icon: LayoutDashboard,
  },
  {
    title: "Assessment",
    path: "/assessment",
    icon: ClipboardCheck,
  },
  {
    title: "AI Chatbot",
    path: "/chatbot",
    icon: MessageSquareHeart,
  },
  {
    title: "Recommendations",
    path: "/recommendations",
    icon: Lightbulb,
  },
  {
    title: "History",
    path: "/history",
    icon: History,
  },
  {
    title: "Emergency",
    path: "/emergency",
    icon: Siren,
  },
  {
    title: "Profile",
    path: "/profile",
    icon: User,
  },
  {
    title: "Settings",
    path: "/settings",
    icon: Settings,
  },
];

export default function Sidebar() {
  return (
    <aside className="hidden md:flex h-screen w-72 flex-col border-r border-slate-200 bg-white dark:border-slate-800 dark:bg-slate-950">

      {/* Logo */}

      <div className="flex items-center gap-3 border-b border-slate-200 px-6 py-6 dark:border-slate-800">

        <div className="flex h-12 w-12 items-center justify-center rounded-2xl bg-gradient-to-r from-indigo-600 to-violet-600 text-white shadow-lg">
          <Brain size={26} />
        </div>

        <div>
          <h1 className="text-xl font-bold text-slate-900 dark:text-white">
            PsyTrack
          </h1>

          <p className="text-xs text-slate-500">
            AI Mental Health
          </p>
        </div>

      </div>

      {/* Menu */}

      <nav className="flex-1 space-y-2 px-4 py-6">

        {menuItems.map((item) => {

          const Icon = item.icon;

          return (
            <NavLink
              key={item.path}
              to={item.path}
              className={({ isActive }) =>
                `flex items-center gap-4 rounded-xl px-4 py-3 transition-all duration-200 ${
                  isActive
                    ? "bg-gradient-to-r from-indigo-600 to-violet-600 text-white shadow-md"
                    : "text-slate-600 hover:bg-slate-100 hover:text-slate-900 dark:text-slate-300 dark:hover:bg-slate-800 dark:hover:text-white"
                }`
              }
            >
              <Icon size={20} />

              <span className="font-medium">
                {item.title}
              </span>
            </NavLink>
          );
        })}

      </nav>

      {/* Footer */}

      <div className="border-t border-slate-200 p-6 dark:border-slate-800">

        <div className="rounded-xl bg-gradient-to-r from-indigo-600 to-violet-600 p-4 text-white">

          <h3 className="font-semibold">
            Mental Wellness
          </h3>

          <p className="mt-2 text-sm text-indigo-100">
            Every step towards better mental health matters.
          </p>

        </div>

      </div>

    </aside>
  );
}