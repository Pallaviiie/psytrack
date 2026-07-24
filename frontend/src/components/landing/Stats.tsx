import AnimatedCounter from "@/components/common/AnimatedCounter";
import { motion } from "framer-motion";
import {
  Users,
  Brain,
  ShieldCheck,
  Heart,
} from "lucide-react";

const stats = [
  {
    icon: Users,
    value: 10000,
    suffix: "+",
    title: "Active Users",
  },
  {
    icon: Brain,
    value: 95,
    suffix: "%",
    title: "AI Accuracy",
  },
  {
    icon: ShieldCheck,
    value: 24,
    suffix: "/7",
    title: "Support",
  },
  {
    icon: Heart,
    value: 500,
    suffix: "+",
    title: "Lives Improved",
  },
];

export default function Stats() {
  return (
    <section className="py-20 bg-violet-50">
      <div className="max-w-7xl mx-auto px-6">

        <h2 className="text-4xl font-bold text-center mb-12">
          Trusted Worldwide
        </h2>

        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-8">

          {stats.map((item, index) => {
            const Icon = item.icon;

            return (
              <motion.div
                key={index}
                whileHover={{
                  y: -10,
                  scale: 1.05,
                }}
                transition={{
                  duration: 0.3,
               }}
               className="bg-white rounded-2xl shadow-lg p-8 text-center"
               >
                <Icon
                  className="mx-auto text-violet-600 mb-5"
                  size={42}
                />

                <h3 className="text-5xl font-bold text-violet-700">
                  <AnimatedCounter end={item.value} />
                  {item.suffix}
                </h3>

                <p className="mt-3 text-lg font-semibold">
                  {item.title}
                </p>
              </motion.div>
            );
          })}

        </div>

      </div>
    </section>
  );
}