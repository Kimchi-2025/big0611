from pathlib import Path
from pypdf import PdfWriter
import re


def natural_sort_key(path):
    """
    파일명을 사람이 보는 숫자 순서대로 정렬
    예:
    file1.pdf
    file2.pdf
    file10.pdf
    """
    return [
        int(text) if text.isdigit() else text.lower()
        for text in re.split(r"(\d+)", path.name)
    ]


# ============================================
# 1. PDF가 들어있는 폴더 경로 입력
# ============================================

folder_input = input("PDF 파일이 들어있는 폴더 경로를 입력하세요: ").strip()

# 따옴표가 포함되어 입력된 경우 제거
folder_input = folder_input.strip('"').strip("'")

folder = Path(folder_input)

if not folder.exists():
    raise FileNotFoundError(f"폴더를 찾을 수 없습니다:\n{folder}")

if not folder.is_dir():
    raise NotADirectoryError(f"폴더 경로가 아닙니다:\n{folder}")


# ============================================
# 2. 폴더 안의 PDF 파일 찾기
# ============================================

output_name = "merged.pdf"
output_path = folder / output_name

pdf_files = [
    file
    for file in folder.iterdir()
    if file.is_file()
    and file.suffix.lower() == ".pdf"
    and file.name != output_name
]


# ============================================
# 3. 파일명 순서대로 정렬
# ============================================

pdf_files = sorted(pdf_files, key=natural_sort_key)

if len(pdf_files) < 2:
    raise ValueError(
        f"병합할 PDF 파일이 2개 이상 필요합니다.\n"
        f"현재 발견된 PDF 파일 수: {len(pdf_files)}"
    )


print("\n병합 순서")
print("-" * 50)

for i, pdf_file in enumerate(pdf_files, start=1):
    print(f"{i}. {pdf_file.name}")


# ============================================
# 4. PDF 이어 붙이기
# ============================================

writer = PdfWriter()

for pdf_file in pdf_files:
    print(f"추가 중: {pdf_file.name}")
    writer.append(str(pdf_file))


# ============================================
# 5. 결과 저장
# ============================================

with open(output_path, "wb") as f:
    writer.write(f)

writer.close()


print("\n" + "=" * 50)
print("PDF 병합 완료")
print(f"저장 위치: {output_path}")
print("=" * 50)