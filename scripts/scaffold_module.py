from pathlib import Path
import sys

from pilot_coach.shared.utils import snake_case


USE_CASE_TEMPLATE = """from dataclasses import dataclass

from pilot_coach.shared.template import BaseUseCase


@dataclass(slots=True)
class {class_name}(BaseUseCase):
    async def run(self, data):
        raise NotImplementedError("Implement business logic here")
"""


def main() -> None:
    if len(sys.argv) != 3:
        print("Usage: uv run python scripts/scaffold_module.py <folder> <ClassName>")
        sys.exit(1)

    folder = Path(sys.argv[1])
    class_name = sys.argv[2]
    file_name = f"{snake_case(class_name)}.py"

    folder.mkdir(parents=True, exist_ok=True)
    output_file = folder / file_name
    output_file.write_text(USE_CASE_TEMPLATE.format(class_name=class_name), encoding="utf-8")
    print(f"Created {output_file}")


if __name__ == "__main__":
    main()
