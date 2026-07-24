import {
  BrainCircuit,
  MessageCircle,
  ShieldAlert,
  HeartPulse,
  BarChart3,
  Sparkles,
} from "lucide-react";

const features = [
  {
    title: "AI Chatbot",
    icon: MessageCircle,
    desc: "Talk with an intelligent AI companion that provides emotional support and guidance.",
  },
  {
    title: "PHQ-9 Assessment",
    icon: BrainCircuit,
    desc: "Scientifically validated mental health assessments for depression screening.",
  },
  {
    title: "Mood Tracking",
    icon: HeartPulse,
    desc: "Monitor your daily emotions and identify long-term mental wellness trends.",
  },
  {
    title: "AI Recommendations",
    icon: Sparkles,
    desc: "Receive personalized wellness suggestions based on your assessments.",
  },
  {
    title: "Emergency Alerts",
    icon: ShieldAlert,
    desc: "Automatically detect high-risk situations and trigger emergency assistance.",
  },
  {
    title: "Analytics Dashboard",
    icon: BarChart3,
    desc: "Visualize your mental wellness journey through interactive charts.",
  },
];

export default function Features() {
  return (
    <section
      id="features"
      className="py-24 bg-slate-50 dark:bg-slate-900"
    >
      <div className="max-w-7xl mx-auto px-6">

        <h2 className="text-5xl font-bold text-center">
          Powerful Features
        </h2>

        <p className="text-center text-slate-500 mt-5 max-w-2xl mx-auto">
          Everything you need to monitor, understand and improve your mental wellness.
        </p>

        <div className="grid lg:grid-cols-3 md:grid-cols-2 gap-8 mt-16">

          {features.map((feature) => (
            <div
              key={feature.title}
              className="rounded-3xl bg-white dark:bg-slate-800 p-8 shadow-lg hover:-translate-y-2 transition"
            >
              <feature.icon
                size={42}
                className="text-violet-600"
              />

              <h3 className="text-2xl font-bold mt-6">
                {feature.title}
              </h3>

              <p className="text-slate-500 mt-4">
                {feature.desc}
              </p>

            </div>
          ))}

        </div>

      </div>
    </section>
  );
}