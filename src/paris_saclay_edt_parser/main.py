from browser import Brwsr, get_events

target_url = "https://edt.universite-paris-saclay.fr/Calendar_DEG_FSO_F2S/cal?vt=agendaDay&dt=2025-09-02&et=group&fid0=LDD3 IM Info-Maths [O3UIM-900 _ O3DIM-910]" 

def main():
    events = get_events(target_url)
    for e in events:
        print(e)
if __name__ == "__main__":
    main()
