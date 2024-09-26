def Hien_thi_tran_dau():
    print("\nChức năng hiển thị trận đấu.\n")

def Them_tran_dau():
    confirm = input("Bạn có chắc chắn muốn thêm trận đấu mới? (Y/N): ")
    if confirm.lower() == 'y':
        print("Chức năng thêm trận đấu.")
    else:
        print("Thao tác đã bị hủy.")

def Tim_kiem():
    print("Chức năng tìm kiếm trận đấu theo tên đội.")

def Cap_nhat_tran_dau():
    confirm = input("Bạn có chắc chắn muốn cập nhật trận đấu? (Y/N): ")
    if confirm.lower() == 'y':
        print("Chức năng cập nhật trận đấu.")
    else:
        print("Thao tác đã bị hủy.")

def Xoa_tran_dau():
    confirm = input("Bạn có chắc chắn muốn xóa trận đấu? (Y/N): ")
    if confirm.lower() == 'y':
        print("Chức năng xóa trận đấu.")
    else:
        print("Thao tác đã bị hủy.")

def Sap_xep_theo_ngay():
    print("Chức năng sắp xếp trận đấu theo ngày.")

def Tinh_toan_hieu_so_ban_thang():
    print("Chức năng tính toán hiệu số theo bàn thắng.")

def menu():
    while True:
        print("\nQuản lý trận đấu bóng đá")
        print("1. Hiển thị danh sách trận đấu")
        print("2. Thêm trận đấu mới")
        print("3. Tìm kiếm trận đấu theo đội")
        print("4. Cập nhật trận đấu")
        print("5. Xóa trận đấu")
        print("6. Sắp xếp trận đấu theo ngày")
        print("7. Tính toán hiệu số bàn thắng")
        print("8. Tính toán hiệu số bàn thắng")
        print("9. Tính toán hiệu số bàn thắng")
        print("10. Xuất dữ liệu")
        print("0. Thoát\n")
        
        choice = input("Chọn chức năng: ")

        if choice == '1':
            Hien_thi_tran_dau()
        elif choice == '2':
            Them_tran_dau()
        elif choice == '3':
            Tim_kiem()
        elif choice == '4':
            Cap_nhat_tran_dau()
        elif choice == '5':
            Xoa_tran_dau()
        elif choice == '6':
            Sap_xep_theo_ngay()
        elif choice == '7':
            Tinh_toan_hieu_so_ban_thang()
        elif choice == '0':
            xac_nhan = input("Xác nhận? (Y/N): ")
            if xac_nhan.lower() == 'y':
                print("Đã thoát chương trình.")
                break
            else:
                print("Thao tác bị hủy.")
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

menu()

