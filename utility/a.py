class Test(View):
    def get(self,request):
        event_results = EventResult.objects.select_related(
            'event_master_id', 'winner_position_id', 'participant_registration_header_id'
        ).filter(is_active=1)

        table_data = []

        for index, result in enumerate(event_results, start=1):
            winner_position = result.winner_position_id.winner_position if result.winner_position_id else None

            # Fetch related EventPrizeMaster for additional details
            event_prize = EventPrizeMaster.objects.filter(
                event_master_id=result.event_master_id,
                winner_position_id=result.winner_position_id
            ).first()

            prize_type = event_prize.prize_type_id.prize_type if event_prize and event_prize.prize_type_id else None
            cash_amount = event_prize.event_cash_prize if event_prize else None

            # Check if ParticipantRegistrationHeader has related ParticipantRegistrationChild
            participant_registration_header = result.participant_registration_header_id
            participant_name = None

            # Get the related ParticipantRegistrationChild data based on the header ID
            participant_registration_child = ParticipantRegistrationChild.objects.filter(
                participant_registration_header_id=participant_registration_header.id
            ).first()

            if participant_registration_child:
                participant_name = participant_registration_child.participant_name

            table_data.append({
                'SlNo': index,
                'Festival': result.event_master_id.festival_master_header_id.festival_name if result.event_master_id else None,
                'EventName': result.event_master_id.event_name if result.event_master_id else None,
                'EventCategory': result.event_master_id.event_category_id.event_category_name if result.event_master_id and result.event_master_id.event_category_id else None,
                'WinnerPosition': winner_position,
                'PrizeType': prize_type,
                'EventScore': event_prize.event_scores if event_prize else None,
                'CollegeName': participant_registration_header.college_name if participant_registration_header else None,
                'ChestNumber': participant_registration_header.event_chest_no if participant_registration_header else None,
                'CashAmount': cash_amount,
                'ParticipantName': participant_name,
                'ID': result.id,
            })

        score = {

        }
        for i in table_data:
            current_score = score.get("CollegeName",0)
            print(f"collage_name : {i['CollegeName']}  score {i['EventScore']}")

            colage_name = i['CollegeName']
            score_event = i['EventScore']
            total_s = score.get(colage_name,0)
            t = score_event+total_s
            score[colage_name]=t
        for d in score:
            print(d)
        return HttpResponse(table_data)