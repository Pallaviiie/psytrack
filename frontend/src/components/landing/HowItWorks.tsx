import {
  UserPlus,
  ClipboardList,
  BrainCircuit,
  Sparkles,
} from "lucide-react";

const steps = [
  {
    icon: UserPlus,
    title: "Create Account",
    desc: "Sign up securely and create your wellness profile.",
  },
  {
    icon: ClipboardList,
    title: "Complete Assessment",
    desc: "Take PHQ-9 and mood assessments.",
  },
  {
    icon: BrainCircuit,
    title: "AI Analysis",
    desc: "Our AI analyzes your responses.",
  },
  {
    icon: Sparkles,
    title: "Get Recommendations",
    desc: "Receive personalized guidance and progress tracking.",
  },
];

export default function HowItWorks() {
  return (
    <section id="how" className="py-24">

      <div className="max-w-6xl mx-auto px-6">

        <h2 className="text-5xl font-bold text-center">
          How PsyTrack Works
        </h2>

        <div className="grid md:grid-cols-4 gap-10 mt-20">

          {steps.map((step, index) => (
            <div
              key={step.title}
              className="text-center"
            >
              <div className="w-20 h-20 rounded-full bg-violet-100 flex items-center justify-center mx-auto">

                <step.icon
                  size={34}
                  className="text-violet-600"
                />

              </div>

              <h3 className="font-bold text-xl mt-6">
                {index + 1}. {step.title}
              </h3>

              <p className="mt-4 text-slate-500">
                {step.desc}
              </p>

            </div>
          ))}

        </div>

      </div>

    </section>
  );
}