import os

def main():
    src_dir = "src"

    def directory_exists(dirname):
        return os.path.isdir(os.path.join(src_dir, dirname))

    def generate_sub_items(parent_folder, indent=1):
        """
        Recursively generate markdown bullet points for subdirectories of parent_folder.
        Each subdirectory must contain a README.md file to be included.
        """
        items = []
        full_path = os.path.join(src_dir, parent_folder)
        if not os.path.isdir(full_path):
            return items

        # Sort entries for deterministic order.
        for entry in sorted(os.listdir(full_path)):
            entry_path = os.path.join(full_path, entry)
            if os.path.isdir(entry_path):
                readme_path = os.path.join(entry_path, "README.md")
                if os.path.isfile(readme_path):
                    bullet = "  " * indent + f"- [{entry}]({parent_folder}/{entry}/README.md)\n"
                    items.append(bullet)
                    # Recursively add any sub-items from this folder.
                    sub_items = generate_sub_items(f"{parent_folder}/{entry}", indent + 1)
                    items.extend(sub_items)
        return items

    # Top-level sections for "Dev" and "Ops"
    ignore_list = ["cpp", "dotnet", "erlang", "go", "java", "javascript", "php", "ruby", "rust", "swift", "other"]
    dev_items = [
        ("cpp", "C++"),
        ("dotnet", ".NET"),
        ("erlang", "Erlang / Elixir"),
        ("go", "Go"),
        ("java", "Java"),
        ("javascript", "JavaScript / TypeScript"),
        ("php", "PHP"),
        ("python", "Python"),
        ("ruby", "Ruby"),
        ("rust", "Rust"),
        ("swift", "Swift"),
        ("other", "Other")
    ]

    ops_items = [
        ("opentelemetry-operator", "OpenTelemetry Operator"),
        ("opentelemetry-collector", "OpenTelemetry Collector")
    ]

    menu = []
    menu.append("# Summary\n\n")
    menu.append("[OpenTelemetry By Example](README.md)\n\n")

    # Dev section
    menu.append("-----------\n")
    for folder, title in dev_items:
        if folder in ignore_list:
            menu.append(f"- [{title}]()\n")
            continue
        if directory_exists(folder):
            menu.append(f"- [{title}]({folder}/README.md)\n")
            # Recursively add subdirectories (if any) as sub-items.
            sub_items = generate_sub_items(folder, indent=1)
            menu.extend(sub_items)

    # Ops section
    menu.append("-----------\n\n")
    for folder, title in ops_items:
        if directory_exists(folder):
            menu.append(f"- [{title}]({folder}/README.md)\n")
            sub_items = generate_sub_items(folder, indent=1)
            menu.extend(sub_items)

    menu.append("\n-----------\n\n")
    menu.append("[Contributors](misc/contributors.md)\n")

    output_file = os.path.join(src_dir, "summary.md")
    with open(output_file, "w", encoding="utf-8") as f:
        f.writelines(menu)

    print(f"summary.md generated successfully at {output_file}")

if __name__ == '__main__':
    main()
