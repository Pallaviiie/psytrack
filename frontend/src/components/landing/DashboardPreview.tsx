import { motion } from "framer-motion";
import {
  Brain,
  Heart,
  Activity,
  Shield,
  TrendingUp,
  CalendarCheck,
} from "lucide-react";

export default function DashboardPreview() {
  return (
    <section className="py-24 bg-gradient-to-b from-white to-violet-50">

      <div className="max-w-7xl mx-auto px-6">

        {/* Heading */}

        <div className="text-center mb-16">

          <h2 className="text-5xl font-bold">
            Your Personal Wellness Dashboard
          </h2>

          <p className="mt-5 text-gray-600 text-lg max-w-3xl mx-auto">
            Monitor your emotional wellbeing, receive AI-powered insights,
            track your mood, and stay connected with your mental health
            journey—all in one place.
          </p>

        </div>

        {/* Dashboard */}

        <motion.div
          initial={{ opacity: 0, y: 80 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.7 }}
          className="rounded-3xl bg-white shadow-2xl border overflow-hidden"
        >

          {/* Top Bar */}

          <div className="bg-violet-700 text-white px-8 py-5 flex justify-between items-center">

            <div>

              <h3 className="text-2xl font-bold">
                Welcome Back 👋
              </h3>

              <p className="text-violet-200">
                Here's today's mental wellness summary
              </p>

            </div>

            <Brain size={45} />

          </div>

          <div className="grid lg:grid-cols-3 gap-6 p-8">

            {/* Mood Score */}

            <motion.div
              whileHover={{ scale: 1.03 }}
              className="rounded-2xl bg-violet-50 p-6"
            >
              <Heart
                className="text-pink-500 mb-4"
                size={40}
              />

              <h4 className="text-gray-500">
                Mood Score
              </h4>

              <h2 className="text-5xl font-bold text-violet-700 mt-2">
                86%
              </h2>

              <p className="text-gray-500 mt-4">
                Your emotional wellbeing has improved this week.
              </p>

            </motion.div>

            {/* Weekly Progress */}

            <motion.div
              whileHover={{ scale: 1.03 }}
              className="rounded-2xl bg-blue-50 p-6"
            >

              <TrendingUp
                className="text-blue-600 mb-4"
                size={40}
              />

              <h4 className="text-gray-500">
                Weekly Progress
              </h4>

              <div className="mt-6 space-y-3">

                <div className="h-3 rounded-full bg-gray-200">
                  <div className="h-3 w-[85%] rounded-full bg-blue-500"></div>
                </div>

                <div className="h-3 rounded-full bg-gray-200">
                  <div className="h-3 w-[60%] rounded-full bg-violet-500"></div>
                </div>

                <div className="h-3 rounded-full bg-gray-200">
                  <div className="h-3 w-[90%] rounded-full bg-green-500"></div>
                </div>

              </div>

              <p className="text-gray-500 mt-6">
                Consistent improvement throughout the week.
              </p>

            </motion.div>

            {/* Emergency */}

            <motion.div
              whileHover={{ scale: 1.03 }}
              className="rounded-2xl bg-green-50 p-6"
            >

              <Shield
                className="text-green-600 mb-4"
                size={40}
              />

              <h4 className="text-gray-500">
                Emergency Status
              </h4>

              <h2 className="text-3xl font-bold text-green-700 mt-3">
                Safe
              </h2>

              <p className="mt-4 text-gray-500">
                No emergency alerts detected.
              </p>

            </motion.div>

            {/* AI Recommendation */}

            <div className="lg:col-span-2 rounded-2xl bg-gray-50 p-6">

              <div className="flex items-center gap-3 mb-5">

                <Activity
                  className="text-violet-600"
                  size={32}
                />

                <h3 className="text-2xl font-bold">
                  AI Recommendations
                </h3>

              </div>

              <ul className="space-y-4">

                <li className="bg-white rounded-xl p-4 shadow-sm">
                  🌿 Take a 10-minute mindful walk today.
                </li>

                <li className="bg-white rounded-xl p-4 shadow-sm">
                  🧘 Practice deep breathing for 5 minutes.
                </li>

                <li className="bg-white rounded-xl p-4 shadow-sm">
                  😴 Maintain at least 8 hours of sleep tonight.
                </li>

              </ul>

            </div>

            {/* Tasks */}

            <div className="rounded-2xl bg-orange-50 p-6">

              <div className="flex items-center gap-3 mb-5">

                <CalendarCheck
                  className="text-orange-500"
                  size={32}
                />

                <h3 className="text-xl font-bold">
                  Today's Tasks
                </h3>

              </div>

              <ul className="space-y-4">

                <li>✅ Drink Water</li>

                <li>✅ Meditation</li>

                <li>⬜ PHQ-9 Assessment</li>

                <li>⬜ Evening Walk</li>

              </ul>

            </div>

          </div>

        </motion.div>

      </div>

    </section>
  );
}