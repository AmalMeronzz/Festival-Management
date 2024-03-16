PGDMP                       |         	   Festivals    16.1    16.1 +   6           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            7           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            8           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            9           1262    16831 	   Festivals    DATABASE     �   CREATE DATABASE "Festivals" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_United States.1252';
    DROP DATABASE "Festivals";
                postgres    false            �            1259    16905 %   AdminMainApp_committemembertypemaster    TABLE     Z  CREATE TABLE public."AdminMainApp_committemembertypemaster" (
    id bigint NOT NULL,
    committe_member_type character varying(50) NOT NULL,
    is_active boolean NOT NULL,
    created_on timestamp with time zone NOT NULL,
    created_by character varying(20),
    modified_on timestamp with time zone,
    modified_by character varying(20)
);
 ;   DROP TABLE public."AdminMainApp_committemembertypemaster";
       public         heap    postgres    false            �            1259    16904 ,   AdminMainApp_committemembertypemaster_id_seq    SEQUENCE     �   CREATE SEQUENCE public."AdminMainApp_committemembertypemaster_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 E   DROP SEQUENCE public."AdminMainApp_committemembertypemaster_id_seq";
       public          postgres    false    228            :           0    0 ,   AdminMainApp_committemembertypemaster_id_seq    SEQUENCE OWNED BY     �   ALTER SEQUENCE public."AdminMainApp_committemembertypemaster_id_seq" OWNED BY public."AdminMainApp_committemembertypemaster".id;
          public          postgres    false    227            �            1259    16871    AdminMainApp_departmentmaster    TABLE     M  CREATE TABLE public."AdminMainApp_departmentmaster" (
    id bigint NOT NULL,
    department_name character varying(50) NOT NULL,
    is_active boolean NOT NULL,
    created_on timestamp with time zone NOT NULL,
    created_by character varying(20),
    modified_on timestamp with time zone,
    modified_by character varying(20)
);
 3   DROP TABLE public."AdminMainApp_departmentmaster";
       public         heap    postgres    false            �            1259    16870 $   AdminMainApp_departmentmaster_id_seq    SEQUENCE     �   CREATE SEQUENCE public."AdminMainApp_departmentmaster_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 =   DROP SEQUENCE public."AdminMainApp_departmentmaster_id_seq";
       public          postgres    false    220            ;           0    0 $   AdminMainApp_departmentmaster_id_seq    SEQUENCE OWNED BY     q   ALTER SEQUENCE public."AdminMainApp_departmentmaster_id_seq" OWNED BY public."AdminMainApp_departmentmaster".id;
          public          postgres    false    219            �            1259    16878     AdminMainApp_eventcategorymaster    TABLE     T  CREATE TABLE public."AdminMainApp_eventcategorymaster" (
    id bigint NOT NULL,
    event_category_name character varying(50) NOT NULL,
    is_active boolean NOT NULL,
    created_on timestamp with time zone NOT NULL,
    created_by character varying(20),
    modified_on timestamp with time zone,
    modified_by character varying(20)
);
 6   DROP TABLE public."AdminMainApp_eventcategorymaster";
       public         heap    postgres    false            �            1259    16877 '   AdminMainApp_eventcategorymaster_id_seq    SEQUENCE     �   CREATE SEQUENCE public."AdminMainApp_eventcategorymaster_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 @   DROP SEQUENCE public."AdminMainApp_eventcategorymaster_id_seq";
       public          postgres    false    222            <           0    0 '   AdminMainApp_eventcategorymaster_id_seq    SEQUENCE OWNED BY     w   ALTER SEQUENCE public."AdminMainApp_eventcategorymaster_id_seq" OWNED BY public."AdminMainApp_eventcategorymaster".id;
          public          postgres    false    221            �            1259    16950    AdminMainApp_eventmaster    TABLE     �  CREATE TABLE public."AdminMainApp_eventmaster" (
    id bigint NOT NULL,
    registration_fee numeric(6,2),
    max_team_size integer,
    min_team_size integer,
    event_description character varying(500),
    is_active boolean NOT NULL,
    created_on timestamp with time zone NOT NULL,
    created_by character varying(20),
    modified_on timestamp with time zone,
    modified_by character varying(20),
    event_category_id_id bigint NOT NULL,
    festival_master_header_id_id bigint NOT NULL,
    participant_category_id_id bigint NOT NULL,
    event_name character varying(80),
    event_type character varying(20),
    event_document character varying(50),
    abbreviation character varying(20)
);
 .   DROP TABLE public."AdminMainApp_eventmaster";
       public         heap    postgres    false            �            1259    16949    AdminMainApp_eventmaster_id_seq    SEQUENCE     �   CREATE SEQUENCE public."AdminMainApp_eventmaster_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 8   DROP SEQUENCE public."AdminMainApp_eventmaster_id_seq";
       public          postgres    false    234            =           0    0    AdminMainApp_eventmaster_id_seq    SEQUENCE OWNED BY     g   ALTER SEQUENCE public."AdminMainApp_eventmaster_id_seq" OWNED BY public."AdminMainApp_eventmaster".id;
          public          postgres    false    233            �            1259    16987    AdminMainApp_eventprizemaster    TABLE     �  CREATE TABLE public."AdminMainApp_eventprizemaster" (
    id bigint NOT NULL,
    is_active boolean NOT NULL,
    created_on timestamp with time zone NOT NULL,
    created_by character varying(20),
    modified_on timestamp with time zone,
    modified_by character varying(20),
    event_master_id_id bigint NOT NULL,
    prize_type_id_id bigint NOT NULL,
    winner_position_id_id bigint NOT NULL,
    event_cash_prize numeric(10,2),
    event_scores numeric(10,2)
);
 3   DROP TABLE public."AdminMainApp_eventprizemaster";
       public         heap    postgres    false            �            1259    16986 $   AdminMainApp_eventprizemaster_id_seq    SEQUENCE     �   CREATE SEQUENCE public."AdminMainApp_eventprizemaster_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 =   DROP SEQUENCE public."AdminMainApp_eventprizemaster_id_seq";
       public          postgres    false    244            >           0    0 $   AdminMainApp_eventprizemaster_id_seq    SEQUENCE OWNED BY     q   ALTER SEQUENCE public."AdminMainApp_eventprizemaster_id_seq" OWNED BY public."AdminMainApp_eventprizemaster".id;
          public          postgres    false    243            �            1259    17088    AdminMainApp_eventresult    TABLE     �  CREATE TABLE public."AdminMainApp_eventresult" (
    id bigint NOT NULL,
    is_active boolean NOT NULL,
    created_on timestamp with time zone NOT NULL,
    created_by character varying(20),
    modified_on timestamp with time zone,
    modified_by character varying(20),
    event_master_id_id bigint NOT NULL,
    participant_registration_header_id_id bigint NOT NULL,
    winner_position_id_id bigint NOT NULL
);
 .   DROP TABLE public."AdminMainApp_eventresult";
       public         heap    postgres    false            �            1259    17087    AdminMainApp_eventresult_id_seq    SEQUENCE     �   CREATE SEQUENCE public."AdminMainApp_eventresult_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 8   DROP SEQUENCE public."AdminMainApp_eventresult_id_seq";
       public          postgres    false    254            ?           0    0    AdminMainApp_eventresult_id_seq    SEQUENCE OWNED BY     g   ALTER SEQUENCE public."AdminMainApp_eventresult_id_seq" OWNED BY public."AdminMainApp_eventresult".id;
          public          postgres    false    253            �            1259    16980    AdminMainApp_eventscheduler    TABLE     s  CREATE TABLE public."AdminMainApp_eventscheduler" (
    id bigint NOT NULL,
    event_start_date date,
    event_end_date date,
    is_active boolean NOT NULL,
    created_on timestamp with time zone NOT NULL,
    created_by character varying(20),
    modified_on timestamp with time zone,
    modified_by character varying(20),
    event_master_id_id bigint NOT NULL
);
 1   DROP TABLE public."AdminMainApp_eventscheduler";
       public         heap    postgres    false            �            1259    16979 "   AdminMainApp_eventscheduler_id_seq    SEQUENCE     �   CREATE SEQUENCE public."AdminMainApp_eventscheduler_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 ;   DROP SEQUENCE public."AdminMainApp_eventscheduler_id_seq";
       public          postgres    false    242            @           0    0 "   AdminMainApp_eventscheduler_id_seq    SEQUENCE OWNED BY     m   ALTER SEQUENCE public."AdminMainApp_eventscheduler_id_seq" OWNED BY public."AdminMainApp_eventscheduler".id;
          public          postgres    false    241            �            1259    16919     AdminMainApp_festivalmasterchild    TABLE     �  CREATE TABLE public."AdminMainApp_festivalmasterchild" (
    id bigint NOT NULL,
    registration_start_date date,
    registration_end_date date,
    is_active boolean NOT NULL,
    created_on timestamp with time zone NOT NULL,
    created_by character varying(20),
    modified_on timestamp with time zone,
    modified_by character varying(20),
    festival_master_header_id_id bigint NOT NULL
);
 6   DROP TABLE public."AdminMainApp_festivalmasterchild";
       public         heap    postgres    false            �            1259    16918 '   AdminMainApp_festivalmasterchild_id_seq    SEQUENCE     �   CREATE SEQUENCE public."AdminMainApp_festivalmasterchild_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 @   DROP SEQUENCE public."AdminMainApp_festivalmasterchild_id_seq";
       public          postgres    false    232            A           0    0 '   AdminMainApp_festivalmasterchild_id_seq    SEQUENCE OWNED BY     w   ALTER SEQUENCE public."AdminMainApp_festivalmasterchild_id_seq" OWNED BY public."AdminMainApp_festivalmasterchild".id;
          public          postgres    false    231            �            1259    16892 !   AdminMainApp_festivalmasterheader    TABLE     �  CREATE TABLE public."AdminMainApp_festivalmasterheader" (
    id bigint NOT NULL,
    festival_name character varying(100) NOT NULL,
    festival_icon character varying(50),
    festival_banner character varying(50),
    from_date date NOT NULL,
    to_date date NOT NULL,
    is_active boolean NOT NULL,
    created_on timestamp with time zone NOT NULL,
    created_by character varying(20),
    modified_on timestamp with time zone,
    modified_by character varying(20)
);
 7   DROP TABLE public."AdminMainApp_festivalmasterheader";
       public         heap    postgres    false            �            1259    16891 (   AdminMainApp_festivalmasterheader_id_seq    SEQUENCE     �   CREATE SEQUENCE public."AdminMainApp_festivalmasterheader_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 A   DROP SEQUENCE public."AdminMainApp_festivalmasterheader_id_seq";
       public          postgres    false    226            B           0    0 (   AdminMainApp_festivalmasterheader_id_seq    SEQUENCE OWNED BY     y   ALTER SEQUENCE public."AdminMainApp_festivalmasterheader_id_seq" OWNED BY public."AdminMainApp_festivalmasterheader".id;
          public          postgres    false    225                        1259    17095    AdminMainApp_gallerymaster    TABLE     g  CREATE TABLE public."AdminMainApp_gallerymaster" (
    id bigint NOT NULL,
    gallery_photo character varying(50),
    is_active boolean NOT NULL,
    created_on timestamp with time zone NOT NULL,
    created_by character varying(20),
    modified_on timestamp with time zone,
    modified_by character varying(20),
    event_result_id_id bigint NOT NULL
);
 0   DROP TABLE public."AdminMainApp_gallerymaster";
       public         heap    postgres    false            �            1259    17094 !   AdminMainApp_gallerymaster_id_seq    SEQUENCE     �   CREATE SEQUENCE public."AdminMainApp_gallerymaster_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 :   DROP SEQUENCE public."AdminMainApp_gallerymaster_id_seq";
       public          postgres    false    256            C           0    0 !   AdminMainApp_gallerymaster_id_seq    SEQUENCE OWNED BY     k   ALTER SEQUENCE public."AdminMainApp_gallerymaster_id_seq" OWNED BY public."AdminMainApp_gallerymaster".id;
          public          postgres    false    255            �            1259    16864    AdminMainApp_institutionmaster    TABLE     �  CREATE TABLE public."AdminMainApp_institutionmaster" (
    id bigint NOT NULL,
    institution_name character varying(100) NOT NULL,
    institution_address character varying(250) NOT NULL,
    institution_phone_no character varying(15),
    institution_icon character varying(50),
    institution_banner character varying(50),
    is_active boolean NOT NULL,
    created_on timestamp with time zone NOT NULL
);
 4   DROP TABLE public."AdminMainApp_institutionmaster";
       public         heap    postgres    false            �            1259    16863 %   AdminMainApp_institutionmaster_id_seq    SEQUENCE     �   CREATE SEQUENCE public."AdminMainApp_institutionmaster_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 >   DROP SEQUENCE public."AdminMainApp_institutionmaster_id_seq";
       public          postgres    false    218            D           0    0 %   AdminMainApp_institutionmaster_id_seq    SEQUENCE OWNED BY     s   ALTER SEQUENCE public."AdminMainApp_institutionmaster_id_seq" OWNED BY public."AdminMainApp_institutionmaster".id;
          public          postgres    false    217            �            1259    16912 %   AdminMainApp_organizingcommittemaster    TABLE     B  CREATE TABLE public."AdminMainApp_organizingcommittemaster" (
    id bigint NOT NULL,
    committe_member_name character varying(70) NOT NULL,
    committe_member_phone character varying(15),
    committe_member_photo character varying(50),
    created_on timestamp with time zone NOT NULL,
    created_by character varying(20),
    modified_on timestamp with time zone,
    modified_by character varying(20),
    committe_member_type_id_id bigint,
    department_master_id_id bigint NOT NULL,
    festival_master_header_id_id bigint NOT NULL,
    is_active boolean NOT NULL
);
 ;   DROP TABLE public."AdminMainApp_organizingcommittemaster";
       public         heap    postgres    false            �            1259    16911 ,   AdminMainApp_organizingcommittemaster_id_seq    SEQUENCE     �   CREATE SEQUENCE public."AdminMainApp_organizingcommittemaster_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 E   DROP SEQUENCE public."AdminMainApp_organizingcommittemaster_id_seq";
       public          postgres    false    230            E           0    0 ,   AdminMainApp_organizingcommittemaster_id_seq    SEQUENCE OWNED BY     �   ALTER SEQUENCE public."AdminMainApp_organizingcommittemaster_id_seq" OWNED BY public."AdminMainApp_organizingcommittemaster".id;
          public          postgres    false    229            �            1259    16885 &   AdminMainApp_participantcategorymaster    TABLE     `  CREATE TABLE public."AdminMainApp_participantcategorymaster" (
    id bigint NOT NULL,
    participant_category_name character varying(50) NOT NULL,
    is_active boolean NOT NULL,
    created_on timestamp with time zone NOT NULL,
    created_by character varying(20),
    modified_on timestamp with time zone,
    modified_by character varying(20)
);
 <   DROP TABLE public."AdminMainApp_participantcategorymaster";
       public         heap    postgres    false            �            1259    16884 -   AdminMainApp_participantcategorymaster_id_seq    SEQUENCE     �   CREATE SEQUENCE public."AdminMainApp_participantcategorymaster_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 F   DROP SEQUENCE public."AdminMainApp_participantcategorymaster_id_seq";
       public          postgres    false    224            F           0    0 -   AdminMainApp_participantcategorymaster_id_seq    SEQUENCE OWNED BY     �   ALTER SEQUENCE public."AdminMainApp_participantcategorymaster_id_seq" OWNED BY public."AdminMainApp_participantcategorymaster".id;
          public          postgres    false    223            �            1259    17057 )   AdminMainApp_participantregistrationchild    TABLE     p  CREATE TABLE public."AdminMainApp_participantregistrationchild" (
    id bigint NOT NULL,
    participant_name character varying(100) NOT NULL,
    participant_id_no character varying(20),
    participant_phone character varying(15),
    participant_id_card character varying(500),
    is_active boolean NOT NULL,
    created_on timestamp with time zone NOT NULL,
    created_by character varying(20),
    modified_on timestamp with time zone,
    modified_by character varying(20),
    participant_registration_header_id_id bigint NOT NULL,
    participant_type_id_id bigint,
    participant_email character varying(50)
);
 ?   DROP TABLE public."AdminMainApp_participantregistrationchild";
       public         heap    postgres    false            �            1259    17056 0   AdminMainApp_participantregistrationchild_id_seq    SEQUENCE     �   CREATE SEQUENCE public."AdminMainApp_participantregistrationchild_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 I   DROP SEQUENCE public."AdminMainApp_participantregistrationchild_id_seq";
       public          postgres    false    252            G           0    0 0   AdminMainApp_participantregistrationchild_id_seq    SEQUENCE OWNED BY     �   ALTER SEQUENCE public."AdminMainApp_participantregistrationchild_id_seq" OWNED BY public."AdminMainApp_participantregistrationchild".id;
          public          postgres    false    251            �            1259    17043 *   AdminMainApp_participantregistrationheader    TABLE     �  CREATE TABLE public."AdminMainApp_participantregistrationheader" (
    id bigint NOT NULL,
    college_name character varying(50),
    event_chest_no character varying(20),
    receipt_no character varying(20),
    is_active boolean NOT NULL,
    created_on timestamp with time zone NOT NULL,
    created_by character varying(20),
    modified_on timestamp with time zone,
    modified_by character varying(20),
    event_master_id_id bigint NOT NULL
);
 @   DROP TABLE public."AdminMainApp_participantregistrationheader";
       public         heap    postgres    false            �            1259    17042 1   AdminMainApp_participantregistrationheader_id_seq    SEQUENCE     �   CREATE SEQUENCE public."AdminMainApp_participantregistrationheader_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 J   DROP SEQUENCE public."AdminMainApp_participantregistrationheader_id_seq";
       public          postgres    false    248            H           0    0 1   AdminMainApp_participantregistrationheader_id_seq    SEQUENCE OWNED BY     �   ALTER SEQUENCE public."AdminMainApp_participantregistrationheader_id_seq" OWNED BY public."AdminMainApp_participantregistrationheader".id;
          public          postgres    false    247            �            1259    17050 +   AdminMainApp_participantregistrationpayment    TABLE     �  CREATE TABLE public."AdminMainApp_participantregistrationpayment" (
    id bigint NOT NULL,
    registration_fee numeric(6,2) NOT NULL,
    payment_status integer NOT NULL,
    is_active boolean NOT NULL,
    created_on timestamp with time zone NOT NULL,
    created_by character varying(20),
    modified_on timestamp with time zone,
    modified_by character varying(20),
    participant_registration_header_id_id bigint NOT NULL,
    payment_type boolean NOT NULL
);
 A   DROP TABLE public."AdminMainApp_participantregistrationpayment";
       public         heap    postgres    false            �            1259    17049 2   AdminMainApp_participantregistrationpayment_id_seq    SEQUENCE     �   CREATE SEQUENCE public."AdminMainApp_participantregistrationpayment_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 K   DROP SEQUENCE public."AdminMainApp_participantregistrationpayment_id_seq";
       public          postgres    false    250            I           0    0 2   AdminMainApp_participantregistrationpayment_id_seq    SEQUENCE OWNED BY     �   ALTER SEQUENCE public."AdminMainApp_participantregistrationpayment_id_seq" OWNED BY public."AdminMainApp_participantregistrationpayment".id;
          public          postgres    false    249            �            1259    17036 "   AdminMainApp_participanttypemaster    TABLE     S  CREATE TABLE public."AdminMainApp_participanttypemaster" (
    id bigint NOT NULL,
    participant_type character varying(50) NOT NULL,
    is_active boolean NOT NULL,
    created_on timestamp with time zone NOT NULL,
    created_by character varying(20),
    modified_on timestamp with time zone,
    modified_by character varying(20)
);
 8   DROP TABLE public."AdminMainApp_participanttypemaster";
       public         heap    postgres    false            �            1259    17035 )   AdminMainApp_participanttypemaster_id_seq    SEQUENCE     �   CREATE SEQUENCE public."AdminMainApp_participanttypemaster_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 B   DROP SEQUENCE public."AdminMainApp_participanttypemaster_id_seq";
       public          postgres    false    246            J           0    0 )   AdminMainApp_participanttypemaster_id_seq    SEQUENCE OWNED BY     {   ALTER SEQUENCE public."AdminMainApp_participanttypemaster_id_seq" OWNED BY public."AdminMainApp_participanttypemaster".id;
          public          postgres    false    245            �            1259    16959 !   AdminMainApp_prizetypemastermodel    TABLE     L  CREATE TABLE public."AdminMainApp_prizetypemastermodel" (
    id bigint NOT NULL,
    prize_type character varying(50) NOT NULL,
    is_active boolean NOT NULL,
    created_on timestamp with time zone NOT NULL,
    created_by character varying(20),
    modified_on timestamp with time zone,
    modified_by character varying(20)
);
 7   DROP TABLE public."AdminMainApp_prizetypemastermodel";
       public         heap    postgres    false            �            1259    16958 #   AdminMainApp_prizetypemaster_id_seq    SEQUENCE     �   CREATE SEQUENCE public."AdminMainApp_prizetypemaster_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 <   DROP SEQUENCE public."AdminMainApp_prizetypemaster_id_seq";
       public          postgres    false    236            K           0    0 #   AdminMainApp_prizetypemaster_id_seq    SEQUENCE OWNED BY     t   ALTER SEQUENCE public."AdminMainApp_prizetypemaster_id_seq" OWNED BY public."AdminMainApp_prizetypemastermodel".id;
          public          postgres    false    235            �            1259    16966    AdminMainApp_sponsormaster    TABLE     �  CREATE TABLE public."AdminMainApp_sponsormaster" (
    id bigint NOT NULL,
    sponsor_name character varying(50) NOT NULL,
    sponsor_logo character varying(50),
    is_active boolean NOT NULL,
    created_on timestamp with time zone NOT NULL,
    created_by character varying(20),
    modified_on timestamp with time zone,
    modified_by character varying(20),
    event_master_id_id bigint,
    festival_master_header_id_id bigint
);
 0   DROP TABLE public."AdminMainApp_sponsormaster";
       public         heap    postgres    false            �            1259    16965 !   AdminMainApp_sponsormaster_id_seq    SEQUENCE     �   CREATE SEQUENCE public."AdminMainApp_sponsormaster_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 :   DROP SEQUENCE public."AdminMainApp_sponsormaster_id_seq";
       public          postgres    false    238            L           0    0 !   AdminMainApp_sponsormaster_id_seq    SEQUENCE OWNED BY     k   ALTER SEQUENCE public."AdminMainApp_sponsormaster_id_seq" OWNED BY public."AdminMainApp_sponsormaster".id;
          public          postgres    false    237                       1259    17133    AdminMainApp_usermaster    TABLE     �  CREATE TABLE public."AdminMainApp_usermaster" (
    id bigint NOT NULL,
    login_id character varying(30) NOT NULL,
    login_password character varying(250) NOT NULL,
    is_active boolean NOT NULL,
    created_on timestamp with time zone NOT NULL,
    created_by character varying(20),
    modified_on timestamp with time zone,
    modified_by character varying(20),
    organizing_committe_master_id_id bigint,
    user_type_id_id bigint NOT NULL
);
 -   DROP TABLE public."AdminMainApp_usermaster";
       public         heap    postgres    false                       1259    17132    AdminMainApp_usermaster_id_seq    SEQUENCE     �   CREATE SEQUENCE public."AdminMainApp_usermaster_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 7   DROP SEQUENCE public."AdminMainApp_usermaster_id_seq";
       public          postgres    false    260            M           0    0    AdminMainApp_usermaster_id_seq    SEQUENCE OWNED BY     e   ALTER SEQUENCE public."AdminMainApp_usermaster_id_seq" OWNED BY public."AdminMainApp_usermaster".id;
          public          postgres    false    259                       1259    17126    AdminMainApp_usertype    TABLE     �   CREATE TABLE public."AdminMainApp_usertype" (
    id bigint NOT NULL,
    usertype character varying(255) NOT NULL,
    is_active boolean NOT NULL
);
 +   DROP TABLE public."AdminMainApp_usertype";
       public         heap    postgres    false                       1259    17125    AdminMainApp_usertype_id_seq    SEQUENCE     �   CREATE SEQUENCE public."AdminMainApp_usertype_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 5   DROP SEQUENCE public."AdminMainApp_usertype_id_seq";
       public          postgres    false    258            N           0    0    AdminMainApp_usertype_id_seq    SEQUENCE OWNED BY     a   ALTER SEQUENCE public."AdminMainApp_usertype_id_seq" OWNED BY public."AdminMainApp_usertype".id;
          public          postgres    false    257            �            1259    16973 &   AdminMainApp_winnerpositionmastermodel    TABLE     V  CREATE TABLE public."AdminMainApp_winnerpositionmastermodel" (
    id bigint NOT NULL,
    winner_position character varying(50) NOT NULL,
    is_active boolean NOT NULL,
    created_on timestamp with time zone NOT NULL,
    created_by character varying(20),
    modified_on timestamp with time zone,
    modified_by character varying(20)
);
 <   DROP TABLE public."AdminMainApp_winnerpositionmastermodel";
       public         heap    postgres    false            �            1259    16972 (   AdminMainApp_winnerpositionmaster_id_seq    SEQUENCE     �   CREATE SEQUENCE public."AdminMainApp_winnerpositionmaster_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 A   DROP SEQUENCE public."AdminMainApp_winnerpositionmaster_id_seq";
       public          postgres    false    240            O           0    0 (   AdminMainApp_winnerpositionmaster_id_seq    SEQUENCE OWNED BY     ~   ALTER SEQUENCE public."AdminMainApp_winnerpositionmaster_id_seq" OWNED BY public."AdminMainApp_winnerpositionmastermodel".id;
          public          postgres    false    239            
           1259    17226 
   auth_group    TABLE     f   CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);
    DROP TABLE public.auth_group;
       public         heap    postgres    false            	           1259    17225    auth_group_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.auth_group_id_seq;
       public          postgres    false    266            P           0    0    auth_group_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;
          public          postgres    false    265                       1259    17235    auth_group_permissions    TABLE     �   CREATE TABLE public.auth_group_permissions (
    id bigint NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);
 *   DROP TABLE public.auth_group_permissions;
       public         heap    postgres    false                       1259    17234    auth_group_permissions_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 4   DROP SEQUENCE public.auth_group_permissions_id_seq;
       public          postgres    false    268            Q           0    0    auth_group_permissions_id_seq    SEQUENCE OWNED BY     _   ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;
          public          postgres    false    267                       1259    17219    auth_permission    TABLE     �   CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);
 #   DROP TABLE public.auth_permission;
       public         heap    postgres    false                       1259    17218    auth_permission_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.auth_permission_id_seq;
       public          postgres    false    264            R           0    0    auth_permission_id_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;
          public          postgres    false    263                       1259    17242 	   auth_user    TABLE     �  CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(150) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);
    DROP TABLE public.auth_user;
       public         heap    postgres    false                       1259    17251    auth_user_groups    TABLE     ~   CREATE TABLE public.auth_user_groups (
    id bigint NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);
 $   DROP TABLE public.auth_user_groups;
       public         heap    postgres    false                       1259    17250    auth_user_groups_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.auth_user_groups_id_seq;
       public          postgres    false    272            S           0    0    auth_user_groups_id_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.auth_user_groups_id_seq OWNED BY public.auth_user_groups.id;
          public          postgres    false    271                       1259    17241    auth_user_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.auth_user_id_seq;
       public          postgres    false    270            T           0    0    auth_user_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.auth_user_id_seq OWNED BY public.auth_user.id;
          public          postgres    false    269                       1259    17258    auth_user_user_permissions    TABLE     �   CREATE TABLE public.auth_user_user_permissions (
    id bigint NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);
 .   DROP TABLE public.auth_user_user_permissions;
       public         heap    postgres    false                       1259    17257 !   auth_user_user_permissions_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 8   DROP SEQUENCE public.auth_user_user_permissions_id_seq;
       public          postgres    false    274            U           0    0 !   auth_user_user_permissions_id_seq    SEQUENCE OWNED BY     g   ALTER SEQUENCE public.auth_user_user_permissions_id_seq OWNED BY public.auth_user_user_permissions.id;
          public          postgres    false    273                       1259    17317    django_admin_log    TABLE     �  CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);
 $   DROP TABLE public.django_admin_log;
       public         heap    postgres    false                       1259    17316    django_admin_log_id_seq    SEQUENCE     �   CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.django_admin_log_id_seq;
       public          postgres    false    276            V           0    0    django_admin_log_id_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;
          public          postgres    false    275                       1259    17210    django_content_type    TABLE     �   CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);
 '   DROP TABLE public.django_content_type;
       public         heap    postgres    false                       1259    17209    django_content_type_id_seq    SEQUENCE     �   CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public.django_content_type_id_seq;
       public          postgres    false    262            W           0    0    django_content_type_id_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;
          public          postgres    false    261            �            1259    16833    django_migrations    TABLE     �   CREATE TABLE public.django_migrations (
    id bigint NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);
 %   DROP TABLE public.django_migrations;
       public         heap    postgres    false            �            1259    16832    django_migrations_id_seq    SEQUENCE     �   CREATE SEQUENCE public.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.django_migrations_id_seq;
       public          postgres    false    216            X           0    0    django_migrations_id_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;
          public          postgres    false    215                       1259    17346    django_session    TABLE     �   CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);
 "   DROP TABLE public.django_session;
       public         heap    postgres    false            �           2604    16908 (   AdminMainApp_committemembertypemaster id    DEFAULT     �   ALTER TABLE ONLY public."AdminMainApp_committemembertypemaster" ALTER COLUMN id SET DEFAULT nextval('public."AdminMainApp_committemembertypemaster_id_seq"'::regclass);
 Y   ALTER TABLE public."AdminMainApp_committemembertypemaster" ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    228    227    228            �           2604    16874     AdminMainApp_departmentmaster id    DEFAULT     �   ALTER TABLE ONLY public."AdminMainApp_departmentmaster" ALTER COLUMN id SET DEFAULT nextval('public."AdminMainApp_departmentmaster_id_seq"'::regclass);
 Q   ALTER TABLE public."AdminMainApp_departmentmaster" ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    219    220    220            �           2604    16881 #   AdminMainApp_eventcategorymaster id    DEFAULT     �   ALTER TABLE ONLY public."AdminMainApp_eventcategorymaster" ALTER COLUMN id SET DEFAULT nextval('public."AdminMainApp_eventcategorymaster_id_seq"'::regclass);
 T   ALTER TABLE public."AdminMainApp_eventcategorymaster" ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    221    222    222            �           2604    16953    AdminMainApp_eventmaster id    DEFAULT     �   ALTER TABLE ONLY public."AdminMainApp_eventmaster" ALTER COLUMN id SET DEFAULT nextval('public."AdminMainApp_eventmaster_id_seq"'::regclass);
 L   ALTER TABLE public."AdminMainApp_eventmaster" ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    233    234    234            �           2604    16990     AdminMainApp_eventprizemaster id    DEFAULT     �   ALTER TABLE ONLY public."AdminMainApp_eventprizemaster" ALTER COLUMN id SET DEFAULT nextval('public."AdminMainApp_eventprizemaster_id_seq"'::regclass);
 Q   ALTER TABLE public."AdminMainApp_eventprizemaster" ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    244    243    244            �           2604    17091    AdminMainApp_eventresult id    DEFAULT     �   ALTER TABLE ONLY public."AdminMainApp_eventresult" ALTER COLUMN id SET DEFAULT nextval('public."AdminMainApp_eventresult_id_seq"'::regclass);
 L   ALTER TABLE public."AdminMainApp_eventresult" ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    253    254    254            �           2604    16983    AdminMainApp_eventscheduler id    DEFAULT     �   ALTER TABLE ONLY public."AdminMainApp_eventscheduler" ALTER COLUMN id SET DEFAULT nextval('public."AdminMainApp_eventscheduler_id_seq"'::regclass);
 O   ALTER TABLE public."AdminMainApp_eventscheduler" ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    242    241    242            �           2604    16922 #   AdminMainApp_festivalmasterchild id    DEFAULT     �   ALTER TABLE ONLY public."AdminMainApp_festivalmasterchild" ALTER COLUMN id SET DEFAULT nextval('public."AdminMainApp_festivalmasterchild_id_seq"'::regclass);
 T   ALTER TABLE public."AdminMainApp_festivalmasterchild" ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    231    232    232            �           2604    16895 $   AdminMainApp_festivalmasterheader id    DEFAULT     �   ALTER TABLE ONLY public."AdminMainApp_festivalmasterheader" ALTER COLUMN id SET DEFAULT nextval('public."AdminMainApp_festivalmasterheader_id_seq"'::regclass);
 U   ALTER TABLE public."AdminMainApp_festivalmasterheader" ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    226    225    226            �           2604    17098    AdminMainApp_gallerymaster id    DEFAULT     �   ALTER TABLE ONLY public."AdminMainApp_gallerymaster" ALTER COLUMN id SET DEFAULT nextval('public."AdminMainApp_gallerymaster_id_seq"'::regclass);
 N   ALTER TABLE public."AdminMainApp_gallerymaster" ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    255    256    256            �           2604    16867 !   AdminMainApp_institutionmaster id    DEFAULT     �   ALTER TABLE ONLY public."AdminMainApp_institutionmaster" ALTER COLUMN id SET DEFAULT nextval('public."AdminMainApp_institutionmaster_id_seq"'::regclass);
 R   ALTER TABLE public."AdminMainApp_institutionmaster" ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    218    217    218            �           2604    16915 (   AdminMainApp_organizingcommittemaster id    DEFAULT     �   ALTER TABLE ONLY public."AdminMainApp_organizingcommittemaster" ALTER COLUMN id SET DEFAULT nextval('public."AdminMainApp_organizingcommittemaster_id_seq"'::regclass);
 Y   ALTER TABLE public."AdminMainApp_organizingcommittemaster" ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    229    230    230            �           2604    16888 )   AdminMainApp_participantcategorymaster id    DEFAULT     �   ALTER TABLE ONLY public."AdminMainApp_participantcategorymaster" ALTER COLUMN id SET DEFAULT nextval('public."AdminMainApp_participantcategorymaster_id_seq"'::regclass);
 Z   ALTER TABLE public."AdminMainApp_participantcategorymaster" ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    223    224    224            �           2604    17060 ,   AdminMainApp_participantregistrationchild id    DEFAULT     �   ALTER TABLE ONLY public."AdminMainApp_participantregistrationchild" ALTER COLUMN id SET DEFAULT nextval('public."AdminMainApp_participantregistrationchild_id_seq"'::regclass);
 ]   ALTER TABLE public."AdminMainApp_participantregistrationchild" ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    251    252    252            �           2604    17046 -   AdminMainApp_participantregistrationheader id    DEFAULT     �   ALTER TABLE ONLY public."AdminMainApp_participantregistrationheader" ALTER COLUMN id SET DEFAULT nextval('public."AdminMainApp_participantregistrationheader_id_seq"'::regclass);
 ^   ALTER TABLE public."AdminMainApp_participantregistrationheader" ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    248    247    248            �           2604    17053 .   AdminMainApp_participantregistrationpayment id    DEFAULT     �   ALTER TABLE ONLY public."AdminMainApp_participantregistrationpayment" ALTER COLUMN id SET DEFAULT nextval('public."AdminMainApp_participantregistrationpayment_id_seq"'::regclass);
 _   ALTER TABLE public."AdminMainApp_participantregistrationpayment" ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    250    249    250            �           2604    17039 %   AdminMainApp_participanttypemaster id    DEFAULT     �   ALTER TABLE ONLY public."AdminMainApp_participanttypemaster" ALTER COLUMN id SET DEFAULT nextval('public."AdminMainApp_participanttypemaster_id_seq"'::regclass);
 V   ALTER TABLE public."AdminMainApp_participanttypemaster" ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    246    245    246            �           2604    16962 $   AdminMainApp_prizetypemastermodel id    DEFAULT     �   ALTER TABLE ONLY public."AdminMainApp_prizetypemastermodel" ALTER COLUMN id SET DEFAULT nextval('public."AdminMainApp_prizetypemaster_id_seq"'::regclass);
 U   ALTER TABLE public."AdminMainApp_prizetypemastermodel" ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    236    235    236            �           2604    16969    AdminMainApp_sponsormaster id    DEFAULT     �   ALTER TABLE ONLY public."AdminMainApp_sponsormaster" ALTER COLUMN id SET DEFAULT nextval('public."AdminMainApp_sponsormaster_id_seq"'::regclass);
 N   ALTER TABLE public."AdminMainApp_sponsormaster" ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    237    238    238            �           2604    17136    AdminMainApp_usermaster id    DEFAULT     �   ALTER TABLE ONLY public."AdminMainApp_usermaster" ALTER COLUMN id SET DEFAULT nextval('public."AdminMainApp_usermaster_id_seq"'::regclass);
 K   ALTER TABLE public."AdminMainApp_usermaster" ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    259    260    260            �           2604    17129    AdminMainApp_usertype id    DEFAULT     �   ALTER TABLE ONLY public."AdminMainApp_usertype" ALTER COLUMN id SET DEFAULT nextval('public."AdminMainApp_usertype_id_seq"'::regclass);
 I   ALTER TABLE public."AdminMainApp_usertype" ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    257    258    258            �           2604    16976 )   AdminMainApp_winnerpositionmastermodel id    DEFAULT     �   ALTER TABLE ONLY public."AdminMainApp_winnerpositionmastermodel" ALTER COLUMN id SET DEFAULT nextval('public."AdminMainApp_winnerpositionmaster_id_seq"'::regclass);
 Z   ALTER TABLE public."AdminMainApp_winnerpositionmastermodel" ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    239    240    240            �           2604    17229    auth_group id    DEFAULT     n   ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);
 <   ALTER TABLE public.auth_group ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    266    265    266            �           2604    17238    auth_group_permissions id    DEFAULT     �   ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);
 H   ALTER TABLE public.auth_group_permissions ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    267    268    268            �           2604    17222    auth_permission id    DEFAULT     x   ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);
 A   ALTER TABLE public.auth_permission ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    263    264    264            �           2604    17245    auth_user id    DEFAULT     l   ALTER TABLE ONLY public.auth_user ALTER COLUMN id SET DEFAULT nextval('public.auth_user_id_seq'::regclass);
 ;   ALTER TABLE public.auth_user ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    270    269    270            �           2604    17254    auth_user_groups id    DEFAULT     z   ALTER TABLE ONLY public.auth_user_groups ALTER COLUMN id SET DEFAULT nextval('public.auth_user_groups_id_seq'::regclass);
 B   ALTER TABLE public.auth_user_groups ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    271    272    272            �           2604    17261    auth_user_user_permissions id    DEFAULT     �   ALTER TABLE ONLY public.auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_user_user_permissions_id_seq'::regclass);
 L   ALTER TABLE public.auth_user_user_permissions ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    273    274    274            �           2604    17320    django_admin_log id    DEFAULT     z   ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);
 B   ALTER TABLE public.django_admin_log ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    275    276    276            �           2604    17213    django_content_type id    DEFAULT     �   ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);
 E   ALTER TABLE public.django_content_type ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    262    261    262            �           2604    16836    django_migrations id    DEFAULT     |   ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);
 C   ALTER TABLE public.django_migrations ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    216    215    216                      0    16905 %   AdminMainApp_committemembertypemaster 
   TABLE DATA           �   COPY public."AdminMainApp_committemembertypemaster" (id, committe_member_type, is_active, created_on, created_by, modified_on, modified_by) FROM stdin;
    public          postgres    false    228   e�      �          0    16871    AdminMainApp_departmentmaster 
   TABLE DATA           �   COPY public."AdminMainApp_departmentmaster" (id, department_name, is_active, created_on, created_by, modified_on, modified_by) FROM stdin;
    public          postgres    false    220   ��      �          0    16878     AdminMainApp_eventcategorymaster 
   TABLE DATA           �   COPY public."AdminMainApp_eventcategorymaster" (id, event_category_name, is_active, created_on, created_by, modified_on, modified_by) FROM stdin;
    public          postgres    false    222   |�                0    16950    AdminMainApp_eventmaster 
   TABLE DATA           >  COPY public."AdminMainApp_eventmaster" (id, registration_fee, max_team_size, min_team_size, event_description, is_active, created_on, created_by, modified_on, modified_by, event_category_id_id, festival_master_header_id_id, participant_category_id_id, event_name, event_type, event_document, abbreviation) FROM stdin;
    public          postgres    false    234   �                0    16987    AdminMainApp_eventprizemaster 
   TABLE DATA           �   COPY public."AdminMainApp_eventprizemaster" (id, is_active, created_on, created_by, modified_on, modified_by, event_master_id_id, prize_type_id_id, winner_position_id_id, event_cash_prize, event_scores) FROM stdin;
    public          postgres    false    244   �                0    17088    AdminMainApp_eventresult 
   TABLE DATA           �   COPY public."AdminMainApp_eventresult" (id, is_active, created_on, created_by, modified_on, modified_by, event_master_id_id, participant_registration_header_id_id, winner_position_id_id) FROM stdin;
    public          postgres    false    254   ��                0    16980    AdminMainApp_eventscheduler 
   TABLE DATA           �   COPY public."AdminMainApp_eventscheduler" (id, event_start_date, event_end_date, is_active, created_on, created_by, modified_on, modified_by, event_master_id_id) FROM stdin;
    public          postgres    false    242   ��                0    16919     AdminMainApp_festivalmasterchild 
   TABLE DATA           �   COPY public."AdminMainApp_festivalmasterchild" (id, registration_start_date, registration_end_date, is_active, created_on, created_by, modified_on, modified_by, festival_master_header_id_id) FROM stdin;
    public          postgres    false    232   ��                 0    16892 !   AdminMainApp_festivalmasterheader 
   TABLE DATA           �   COPY public."AdminMainApp_festivalmasterheader" (id, festival_name, festival_icon, festival_banner, from_date, to_date, is_active, created_on, created_by, modified_on, modified_by) FROM stdin;
    public          postgres    false    226   ��                0    17095    AdminMainApp_gallerymaster 
   TABLE DATA           �   COPY public."AdminMainApp_gallerymaster" (id, gallery_photo, is_active, created_on, created_by, modified_on, modified_by, event_result_id_id) FROM stdin;
    public          postgres    false    256   ��      �          0    16864    AdminMainApp_institutionmaster 
   TABLE DATA           �   COPY public."AdminMainApp_institutionmaster" (id, institution_name, institution_address, institution_phone_no, institution_icon, institution_banner, is_active, created_on) FROM stdin;
    public          postgres    false    218   ��                0    16912 %   AdminMainApp_organizingcommittemaster 
   TABLE DATA             COPY public."AdminMainApp_organizingcommittemaster" (id, committe_member_name, committe_member_phone, committe_member_photo, created_on, created_by, modified_on, modified_by, committe_member_type_id_id, department_master_id_id, festival_master_header_id_id, is_active) FROM stdin;
    public          postgres    false    230   ��      �          0    16885 &   AdminMainApp_participantcategorymaster 
   TABLE DATA           �   COPY public."AdminMainApp_participantcategorymaster" (id, participant_category_name, is_active, created_on, created_by, modified_on, modified_by) FROM stdin;
    public          postgres    false    224   ��                0    17057 )   AdminMainApp_participantregistrationchild 
   TABLE DATA           %  COPY public."AdminMainApp_participantregistrationchild" (id, participant_name, participant_id_no, participant_phone, participant_id_card, is_active, created_on, created_by, modified_on, modified_by, participant_registration_header_id_id, participant_type_id_id, participant_email) FROM stdin;
    public          postgres    false    252   �                0    17043 *   AdminMainApp_participantregistrationheader 
   TABLE DATA           �   COPY public."AdminMainApp_participantregistrationheader" (id, college_name, event_chest_no, receipt_no, is_active, created_on, created_by, modified_on, modified_by, event_master_id_id) FROM stdin;
    public          postgres    false    248   S�                0    17050 +   AdminMainApp_participantregistrationpayment 
   TABLE DATA           �   COPY public."AdminMainApp_participantregistrationpayment" (id, registration_fee, payment_status, is_active, created_on, created_by, modified_on, modified_by, participant_registration_header_id_id, payment_type) FROM stdin;
    public          postgres    false    250   s�                0    17036 "   AdminMainApp_participanttypemaster 
   TABLE DATA           �   COPY public."AdminMainApp_participanttypemaster" (id, participant_type, is_active, created_on, created_by, modified_on, modified_by) FROM stdin;
    public          postgres    false    246   =�      
          0    16959 !   AdminMainApp_prizetypemastermodel 
   TABLE DATA           �   COPY public."AdminMainApp_prizetypemastermodel" (id, prize_type, is_active, created_on, created_by, modified_on, modified_by) FROM stdin;
    public          postgres    false    236   ��                0    16966    AdminMainApp_sponsormaster 
   TABLE DATA           �   COPY public."AdminMainApp_sponsormaster" (id, sponsor_name, sponsor_logo, is_active, created_on, created_by, modified_on, modified_by, event_master_id_id, festival_master_header_id_id) FROM stdin;
    public          postgres    false    238   I�      "          0    17133    AdminMainApp_usermaster 
   TABLE DATA           �   COPY public."AdminMainApp_usermaster" (id, login_id, login_password, is_active, created_on, created_by, modified_on, modified_by, organizing_committe_master_id_id, user_type_id_id) FROM stdin;
    public          postgres    false    260   ��                 0    17126    AdminMainApp_usertype 
   TABLE DATA           J   COPY public."AdminMainApp_usertype" (id, usertype, is_active) FROM stdin;
    public          postgres    false    258   d�                0    16973 &   AdminMainApp_winnerpositionmastermodel 
   TABLE DATA           �   COPY public."AdminMainApp_winnerpositionmastermodel" (id, winner_position, is_active, created_on, created_by, modified_on, modified_by) FROM stdin;
    public          postgres    false    240   ��      (          0    17226 
   auth_group 
   TABLE DATA           .   COPY public.auth_group (id, name) FROM stdin;
    public          postgres    false    266   =�      *          0    17235    auth_group_permissions 
   TABLE DATA           M   COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
    public          postgres    false    268   Z�      &          0    17219    auth_permission 
   TABLE DATA           N   COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
    public          postgres    false    264   w�      ,          0    17242 	   auth_user 
   TABLE DATA           �   COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
    public          postgres    false    270   P�      .          0    17251    auth_user_groups 
   TABLE DATA           A   COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
    public          postgres    false    272   m�      0          0    17258    auth_user_user_permissions 
   TABLE DATA           P   COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
    public          postgres    false    274   ��      2          0    17317    django_admin_log 
   TABLE DATA           �   COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
    public          postgres    false    276   ��      $          0    17210    django_content_type 
   TABLE DATA           C   COPY public.django_content_type (id, app_label, model) FROM stdin;
    public          postgres    false    262   ��      �          0    16833    django_migrations 
   TABLE DATA           C   COPY public.django_migrations (id, app, name, applied) FROM stdin;
    public          postgres    false    216   �      3          0    17346    django_session 
   TABLE DATA           P   COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
    public          postgres    false    277   a�      Y           0    0 ,   AdminMainApp_committemembertypemaster_id_seq    SEQUENCE SET     \   SELECT pg_catalog.setval('public."AdminMainApp_committemembertypemaster_id_seq"', 5, true);
          public          postgres    false    227            Z           0    0 $   AdminMainApp_departmentmaster_id_seq    SEQUENCE SET     T   SELECT pg_catalog.setval('public."AdminMainApp_departmentmaster_id_seq"', 3, true);
          public          postgres    false    219            [           0    0 '   AdminMainApp_eventcategorymaster_id_seq    SEQUENCE SET     W   SELECT pg_catalog.setval('public."AdminMainApp_eventcategorymaster_id_seq"', 4, true);
          public          postgres    false    221            \           0    0    AdminMainApp_eventmaster_id_seq    SEQUENCE SET     O   SELECT pg_catalog.setval('public."AdminMainApp_eventmaster_id_seq"', 5, true);
          public          postgres    false    233            ]           0    0 $   AdminMainApp_eventprizemaster_id_seq    SEQUENCE SET     T   SELECT pg_catalog.setval('public."AdminMainApp_eventprizemaster_id_seq"', 2, true);
          public          postgres    false    243            ^           0    0    AdminMainApp_eventresult_id_seq    SEQUENCE SET     P   SELECT pg_catalog.setval('public."AdminMainApp_eventresult_id_seq"', 14, true);
          public          postgres    false    253            _           0    0 "   AdminMainApp_eventscheduler_id_seq    SEQUENCE SET     R   SELECT pg_catalog.setval('public."AdminMainApp_eventscheduler_id_seq"', 5, true);
          public          postgres    false    241            `           0    0 '   AdminMainApp_festivalmasterchild_id_seq    SEQUENCE SET     W   SELECT pg_catalog.setval('public."AdminMainApp_festivalmasterchild_id_seq"', 2, true);
          public          postgres    false    231            a           0    0 (   AdminMainApp_festivalmasterheader_id_seq    SEQUENCE SET     X   SELECT pg_catalog.setval('public."AdminMainApp_festivalmasterheader_id_seq"', 2, true);
          public          postgres    false    225            b           0    0 !   AdminMainApp_gallerymaster_id_seq    SEQUENCE SET     R   SELECT pg_catalog.setval('public."AdminMainApp_gallerymaster_id_seq"', 1, false);
          public          postgres    false    255            c           0    0 %   AdminMainApp_institutionmaster_id_seq    SEQUENCE SET     V   SELECT pg_catalog.setval('public."AdminMainApp_institutionmaster_id_seq"', 1, false);
          public          postgres    false    217            d           0    0 ,   AdminMainApp_organizingcommittemaster_id_seq    SEQUENCE SET     \   SELECT pg_catalog.setval('public."AdminMainApp_organizingcommittemaster_id_seq"', 7, true);
          public          postgres    false    229            e           0    0 -   AdminMainApp_participantcategorymaster_id_seq    SEQUENCE SET     ]   SELECT pg_catalog.setval('public."AdminMainApp_participantcategorymaster_id_seq"', 2, true);
          public          postgres    false    223            f           0    0 0   AdminMainApp_participantregistrationchild_id_seq    SEQUENCE SET     a   SELECT pg_catalog.setval('public."AdminMainApp_participantregistrationchild_id_seq"', 29, true);
          public          postgres    false    251            g           0    0 1   AdminMainApp_participantregistrationheader_id_seq    SEQUENCE SET     b   SELECT pg_catalog.setval('public."AdminMainApp_participantregistrationheader_id_seq"', 41, true);
          public          postgres    false    247            h           0    0 2   AdminMainApp_participantregistrationpayment_id_seq    SEQUENCE SET     c   SELECT pg_catalog.setval('public."AdminMainApp_participantregistrationpayment_id_seq"', 26, true);
          public          postgres    false    249            i           0    0 )   AdminMainApp_participanttypemaster_id_seq    SEQUENCE SET     Y   SELECT pg_catalog.setval('public."AdminMainApp_participanttypemaster_id_seq"', 3, true);
          public          postgres    false    245            j           0    0 #   AdminMainApp_prizetypemaster_id_seq    SEQUENCE SET     S   SELECT pg_catalog.setval('public."AdminMainApp_prizetypemaster_id_seq"', 3, true);
          public          postgres    false    235            k           0    0 !   AdminMainApp_sponsormaster_id_seq    SEQUENCE SET     Q   SELECT pg_catalog.setval('public."AdminMainApp_sponsormaster_id_seq"', 2, true);
          public          postgres    false    237            l           0    0    AdminMainApp_usermaster_id_seq    SEQUENCE SET     N   SELECT pg_catalog.setval('public."AdminMainApp_usermaster_id_seq"', 3, true);
          public          postgres    false    259            m           0    0    AdminMainApp_usertype_id_seq    SEQUENCE SET     L   SELECT pg_catalog.setval('public."AdminMainApp_usertype_id_seq"', 4, true);
          public          postgres    false    257            n           0    0 (   AdminMainApp_winnerpositionmaster_id_seq    SEQUENCE SET     X   SELECT pg_catalog.setval('public."AdminMainApp_winnerpositionmaster_id_seq"', 4, true);
          public          postgres    false    239            o           0    0    auth_group_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);
          public          postgres    false    265            p           0    0    auth_group_permissions_id_seq    SEQUENCE SET     L   SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);
          public          postgres    false    267            q           0    0    auth_permission_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.auth_permission_id_seq', 132, true);
          public          postgres    false    263            r           0    0    auth_user_groups_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);
          public          postgres    false    271            s           0    0    auth_user_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.auth_user_id_seq', 1, false);
          public          postgres    false    269            t           0    0 !   auth_user_user_permissions_id_seq    SEQUENCE SET     P   SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);
          public          postgres    false    273            u           0    0    django_admin_log_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.django_admin_log_id_seq', 1, false);
          public          postgres    false    275            v           0    0    django_content_type_id_seq    SEQUENCE SET     I   SELECT pg_catalog.setval('public.django_content_type_id_seq', 33, true);
          public          postgres    false    261            w           0    0    django_migrations_id_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public.django_migrations_id_seq', 69, true);
          public          postgres    false    215            �           2606    16910 P   AdminMainApp_committemembertypemaster AdminMainApp_committemembertypemaster_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public."AdminMainApp_committemembertypemaster"
    ADD CONSTRAINT "AdminMainApp_committemembertypemaster_pkey" PRIMARY KEY (id);
 ~   ALTER TABLE ONLY public."AdminMainApp_committemembertypemaster" DROP CONSTRAINT "AdminMainApp_committemembertypemaster_pkey";
       public            postgres    false    228            �           2606    16876 @   AdminMainApp_departmentmaster AdminMainApp_departmentmaster_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public."AdminMainApp_departmentmaster"
    ADD CONSTRAINT "AdminMainApp_departmentmaster_pkey" PRIMARY KEY (id);
 n   ALTER TABLE ONLY public."AdminMainApp_departmentmaster" DROP CONSTRAINT "AdminMainApp_departmentmaster_pkey";
       public            postgres    false    220            �           2606    16883 F   AdminMainApp_eventcategorymaster AdminMainApp_eventcategorymaster_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public."AdminMainApp_eventcategorymaster"
    ADD CONSTRAINT "AdminMainApp_eventcategorymaster_pkey" PRIMARY KEY (id);
 t   ALTER TABLE ONLY public."AdminMainApp_eventcategorymaster" DROP CONSTRAINT "AdminMainApp_eventcategorymaster_pkey";
       public            postgres    false    222            �           2606    16957 6   AdminMainApp_eventmaster AdminMainApp_eventmaster_pkey 
   CONSTRAINT     x   ALTER TABLE ONLY public."AdminMainApp_eventmaster"
    ADD CONSTRAINT "AdminMainApp_eventmaster_pkey" PRIMARY KEY (id);
 d   ALTER TABLE ONLY public."AdminMainApp_eventmaster" DROP CONSTRAINT "AdminMainApp_eventmaster_pkey";
       public            postgres    false    234            �           2606    16992 @   AdminMainApp_eventprizemaster AdminMainApp_eventprizemaster_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public."AdminMainApp_eventprizemaster"
    ADD CONSTRAINT "AdminMainApp_eventprizemaster_pkey" PRIMARY KEY (id);
 n   ALTER TABLE ONLY public."AdminMainApp_eventprizemaster" DROP CONSTRAINT "AdminMainApp_eventprizemaster_pkey";
       public            postgres    false    244                       2606    17093 6   AdminMainApp_eventresult AdminMainApp_eventresult_pkey 
   CONSTRAINT     x   ALTER TABLE ONLY public."AdminMainApp_eventresult"
    ADD CONSTRAINT "AdminMainApp_eventresult_pkey" PRIMARY KEY (id);
 d   ALTER TABLE ONLY public."AdminMainApp_eventresult" DROP CONSTRAINT "AdminMainApp_eventresult_pkey";
       public            postgres    false    254            �           2606    16985 <   AdminMainApp_eventscheduler AdminMainApp_eventscheduler_pkey 
   CONSTRAINT     ~   ALTER TABLE ONLY public."AdminMainApp_eventscheduler"
    ADD CONSTRAINT "AdminMainApp_eventscheduler_pkey" PRIMARY KEY (id);
 j   ALTER TABLE ONLY public."AdminMainApp_eventscheduler" DROP CONSTRAINT "AdminMainApp_eventscheduler_pkey";
       public            postgres    false    242            �           2606    16924 F   AdminMainApp_festivalmasterchild AdminMainApp_festivalmasterchild_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public."AdminMainApp_festivalmasterchild"
    ADD CONSTRAINT "AdminMainApp_festivalmasterchild_pkey" PRIMARY KEY (id);
 t   ALTER TABLE ONLY public."AdminMainApp_festivalmasterchild" DROP CONSTRAINT "AdminMainApp_festivalmasterchild_pkey";
       public            postgres    false    232            �           2606    16897 H   AdminMainApp_festivalmasterheader AdminMainApp_festivalmasterheader_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public."AdminMainApp_festivalmasterheader"
    ADD CONSTRAINT "AdminMainApp_festivalmasterheader_pkey" PRIMARY KEY (id);
 v   ALTER TABLE ONLY public."AdminMainApp_festivalmasterheader" DROP CONSTRAINT "AdminMainApp_festivalmasterheader_pkey";
       public            postgres    false    226                       2606    17100 :   AdminMainApp_gallerymaster AdminMainApp_gallerymaster_pkey 
   CONSTRAINT     |   ALTER TABLE ONLY public."AdminMainApp_gallerymaster"
    ADD CONSTRAINT "AdminMainApp_gallerymaster_pkey" PRIMARY KEY (id);
 h   ALTER TABLE ONLY public."AdminMainApp_gallerymaster" DROP CONSTRAINT "AdminMainApp_gallerymaster_pkey";
       public            postgres    false    256            �           2606    16869 B   AdminMainApp_institutionmaster AdminMainApp_institutionmaster_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public."AdminMainApp_institutionmaster"
    ADD CONSTRAINT "AdminMainApp_institutionmaster_pkey" PRIMARY KEY (id);
 p   ALTER TABLE ONLY public."AdminMainApp_institutionmaster" DROP CONSTRAINT "AdminMainApp_institutionmaster_pkey";
       public            postgres    false    218            �           2606    16917 P   AdminMainApp_organizingcommittemaster AdminMainApp_organizingcommittemaster_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public."AdminMainApp_organizingcommittemaster"
    ADD CONSTRAINT "AdminMainApp_organizingcommittemaster_pkey" PRIMARY KEY (id);
 ~   ALTER TABLE ONLY public."AdminMainApp_organizingcommittemaster" DROP CONSTRAINT "AdminMainApp_organizingcommittemaster_pkey";
       public            postgres    false    230            �           2606    16890 R   AdminMainApp_participantcategorymaster AdminMainApp_participantcategorymaster_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public."AdminMainApp_participantcategorymaster"
    ADD CONSTRAINT "AdminMainApp_participantcategorymaster_pkey" PRIMARY KEY (id);
 �   ALTER TABLE ONLY public."AdminMainApp_participantcategorymaster" DROP CONSTRAINT "AdminMainApp_participantcategorymaster_pkey";
       public            postgres    false    224            
           2606    17062 X   AdminMainApp_participantregistrationchild AdminMainApp_participantregistrationchild_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public."AdminMainApp_participantregistrationchild"
    ADD CONSTRAINT "AdminMainApp_participantregistrationchild_pkey" PRIMARY KEY (id);
 �   ALTER TABLE ONLY public."AdminMainApp_participantregistrationchild" DROP CONSTRAINT "AdminMainApp_participantregistrationchild_pkey";
       public            postgres    false    252                       2606    17048 Z   AdminMainApp_participantregistrationheader AdminMainApp_participantregistrationheader_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public."AdminMainApp_participantregistrationheader"
    ADD CONSTRAINT "AdminMainApp_participantregistrationheader_pkey" PRIMARY KEY (id);
 �   ALTER TABLE ONLY public."AdminMainApp_participantregistrationheader" DROP CONSTRAINT "AdminMainApp_participantregistrationheader_pkey";
       public            postgres    false    248                       2606    17055 \   AdminMainApp_participantregistrationpayment AdminMainApp_participantregistrationpayment_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public."AdminMainApp_participantregistrationpayment"
    ADD CONSTRAINT "AdminMainApp_participantregistrationpayment_pkey" PRIMARY KEY (id);
 �   ALTER TABLE ONLY public."AdminMainApp_participantregistrationpayment" DROP CONSTRAINT "AdminMainApp_participantregistrationpayment_pkey";
       public            postgres    false    250                        2606    17041 J   AdminMainApp_participanttypemaster AdminMainApp_participanttypemaster_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public."AdminMainApp_participanttypemaster"
    ADD CONSTRAINT "AdminMainApp_participanttypemaster_pkey" PRIMARY KEY (id);
 x   ALTER TABLE ONLY public."AdminMainApp_participanttypemaster" DROP CONSTRAINT "AdminMainApp_participanttypemaster_pkey";
       public            postgres    false    246            �           2606    16964 C   AdminMainApp_prizetypemastermodel AdminMainApp_prizetypemaster_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public."AdminMainApp_prizetypemastermodel"
    ADD CONSTRAINT "AdminMainApp_prizetypemaster_pkey" PRIMARY KEY (id);
 q   ALTER TABLE ONLY public."AdminMainApp_prizetypemastermodel" DROP CONSTRAINT "AdminMainApp_prizetypemaster_pkey";
       public            postgres    false    236            �           2606    16971 :   AdminMainApp_sponsormaster AdminMainApp_sponsormaster_pkey 
   CONSTRAINT     |   ALTER TABLE ONLY public."AdminMainApp_sponsormaster"
    ADD CONSTRAINT "AdminMainApp_sponsormaster_pkey" PRIMARY KEY (id);
 h   ALTER TABLE ONLY public."AdminMainApp_sponsormaster" DROP CONSTRAINT "AdminMainApp_sponsormaster_pkey";
       public            postgres    false    238                       2606    17138 4   AdminMainApp_usermaster AdminMainApp_usermaster_pkey 
   CONSTRAINT     v   ALTER TABLE ONLY public."AdminMainApp_usermaster"
    ADD CONSTRAINT "AdminMainApp_usermaster_pkey" PRIMARY KEY (id);
 b   ALTER TABLE ONLY public."AdminMainApp_usermaster" DROP CONSTRAINT "AdminMainApp_usermaster_pkey";
       public            postgres    false    260                       2606    17131 0   AdminMainApp_usertype AdminMainApp_usertype_pkey 
   CONSTRAINT     r   ALTER TABLE ONLY public."AdminMainApp_usertype"
    ADD CONSTRAINT "AdminMainApp_usertype_pkey" PRIMARY KEY (id);
 ^   ALTER TABLE ONLY public."AdminMainApp_usertype" DROP CONSTRAINT "AdminMainApp_usertype_pkey";
       public            postgres    false    258            �           2606    16978 M   AdminMainApp_winnerpositionmastermodel AdminMainApp_winnerpositionmaster_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public."AdminMainApp_winnerpositionmastermodel"
    ADD CONSTRAINT "AdminMainApp_winnerpositionmaster_pkey" PRIMARY KEY (id);
 {   ALTER TABLE ONLY public."AdminMainApp_winnerpositionmastermodel" DROP CONSTRAINT "AdminMainApp_winnerpositionmaster_pkey";
       public            postgres    false    240            $           2606    17344    auth_group auth_group_name_key 
   CONSTRAINT     Y   ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);
 H   ALTER TABLE ONLY public.auth_group DROP CONSTRAINT auth_group_name_key;
       public            postgres    false    266            )           2606    17274 R   auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);
 |   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq;
       public            postgres    false    268    268            ,           2606    17240 2   auth_group_permissions auth_group_permissions_pkey 
   CONSTRAINT     p   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);
 \   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_pkey;
       public            postgres    false    268            &           2606    17231    auth_group auth_group_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);
 D   ALTER TABLE ONLY public.auth_group DROP CONSTRAINT auth_group_pkey;
       public            postgres    false    266                       2606    17265 F   auth_permission auth_permission_content_type_id_codename_01ab375a_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);
 p   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq;
       public            postgres    false    264    264            !           2606    17224 $   auth_permission auth_permission_pkey 
   CONSTRAINT     b   ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);
 N   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_pkey;
       public            postgres    false    264            4           2606    17256 &   auth_user_groups auth_user_groups_pkey 
   CONSTRAINT     d   ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);
 P   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_pkey;
       public            postgres    false    272            7           2606    17289 @   auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);
 j   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq;
       public            postgres    false    272    272            .           2606    17247    auth_user auth_user_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);
 B   ALTER TABLE ONLY public.auth_user DROP CONSTRAINT auth_user_pkey;
       public            postgres    false    270            :           2606    17263 :   auth_user_user_permissions auth_user_user_permissions_pkey 
   CONSTRAINT     x   ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);
 d   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_pkey;
       public            postgres    false    274            =           2606    17303 Y   auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);
 �   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq;
       public            postgres    false    274    274            1           2606    17339     auth_user auth_user_username_key 
   CONSTRAINT     _   ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);
 J   ALTER TABLE ONLY public.auth_user DROP CONSTRAINT auth_user_username_key;
       public            postgres    false    270            @           2606    17325 &   django_admin_log django_admin_log_pkey 
   CONSTRAINT     d   ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);
 P   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_pkey;
       public            postgres    false    276                       2606    17217 E   django_content_type django_content_type_app_label_model_76bd3d3b_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);
 o   ALTER TABLE ONLY public.django_content_type DROP CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq;
       public            postgres    false    262    262                       2606    17215 ,   django_content_type django_content_type_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);
 V   ALTER TABLE ONLY public.django_content_type DROP CONSTRAINT django_content_type_pkey;
       public            postgres    false    262            �           2606    16840 (   django_migrations django_migrations_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);
 R   ALTER TABLE ONLY public.django_migrations DROP CONSTRAINT django_migrations_pkey;
       public            postgres    false    216            D           2606    17352 "   django_session django_session_pkey 
   CONSTRAINT     i   ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);
 L   ALTER TABLE ONLY public.django_session DROP CONSTRAINT django_session_pkey;
       public            postgres    false    277            �           1259    17008 6   AdminMainApp_eventmaster_event_category_id_id_44ba300b    INDEX     �   CREATE INDEX "AdminMainApp_eventmaster_event_category_id_id_44ba300b" ON public."AdminMainApp_eventmaster" USING btree (event_category_id_id);
 L   DROP INDEX public."AdminMainApp_eventmaster_event_category_id_id_44ba300b";
       public            postgres    false    234            �           1259    17009 >   AdminMainApp_eventmaster_festival_master_header_id_id_a341fcc1    INDEX     �   CREATE INDEX "AdminMainApp_eventmaster_festival_master_header_id_id_a341fcc1" ON public."AdminMainApp_eventmaster" USING btree (festival_master_header_id_id);
 T   DROP INDEX public."AdminMainApp_eventmaster_festival_master_header_id_id_a341fcc1";
       public            postgres    false    234            �           1259    17010 <   AdminMainApp_eventmaster_participant_category_id_id_629bd6c4    INDEX     �   CREATE INDEX "AdminMainApp_eventmaster_participant_category_id_id_629bd6c4" ON public."AdminMainApp_eventmaster" USING btree (participant_category_id_id);
 R   DROP INDEX public."AdminMainApp_eventmaster_participant_category_id_id_629bd6c4";
       public            postgres    false    234            �           1259    17032 9   AdminMainApp_eventprizemaster_event_master_id_id_752a39f0    INDEX     �   CREATE INDEX "AdminMainApp_eventprizemaster_event_master_id_id_752a39f0" ON public."AdminMainApp_eventprizemaster" USING btree (event_master_id_id);
 O   DROP INDEX public."AdminMainApp_eventprizemaster_event_master_id_id_752a39f0";
       public            postgres    false    244            �           1259    17033 7   AdminMainApp_eventprizemaster_prize_type_id_id_eb4004f8    INDEX     �   CREATE INDEX "AdminMainApp_eventprizemaster_prize_type_id_id_eb4004f8" ON public."AdminMainApp_eventprizemaster" USING btree (prize_type_id_id);
 M   DROP INDEX public."AdminMainApp_eventprizemaster_prize_type_id_id_eb4004f8";
       public            postgres    false    244            �           1259    17034 <   AdminMainApp_eventprizemaster_winner_position_id_id_79f6e072    INDEX     �   CREATE INDEX "AdminMainApp_eventprizemaster_winner_position_id_id_79f6e072" ON public."AdminMainApp_eventprizemaster" USING btree (winner_position_id_id);
 R   DROP INDEX public."AdminMainApp_eventprizemaster_winner_position_id_id_79f6e072";
       public            postgres    false    244                       1259    17116 4   AdminMainApp_eventresult_event_master_id_id_8b3a227a    INDEX     �   CREATE INDEX "AdminMainApp_eventresult_event_master_id_id_8b3a227a" ON public."AdminMainApp_eventresult" USING btree (event_master_id_id);
 J   DROP INDEX public."AdminMainApp_eventresult_event_master_id_id_8b3a227a";
       public            postgres    false    254                       1259    17117 <   AdminMainApp_eventresult_participant_registration_h_d10b5911    INDEX     �   CREATE INDEX "AdminMainApp_eventresult_participant_registration_h_d10b5911" ON public."AdminMainApp_eventresult" USING btree (participant_registration_header_id_id);
 R   DROP INDEX public."AdminMainApp_eventresult_participant_registration_h_d10b5911";
       public            postgres    false    254                       1259    17118 7   AdminMainApp_eventresult_winner_position_id_id_6ee0ea91    INDEX     �   CREATE INDEX "AdminMainApp_eventresult_winner_position_id_id_6ee0ea91" ON public."AdminMainApp_eventresult" USING btree (winner_position_id_id);
 M   DROP INDEX public."AdminMainApp_eventresult_winner_position_id_id_6ee0ea91";
       public            postgres    false    254            �           1259    17016 7   AdminMainApp_eventscheduler_event_master_id_id_6a1b8acd    INDEX     �   CREATE INDEX "AdminMainApp_eventscheduler_event_master_id_id_6a1b8acd" ON public."AdminMainApp_eventscheduler" USING btree (event_master_id_id);
 M   DROP INDEX public."AdminMainApp_eventscheduler_event_master_id_id_6a1b8acd";
       public            postgres    false    242            �           1259    16948 >   AdminMainApp_festivalmaste_festival_master_header_id__a65f92d6    INDEX     �   CREATE INDEX "AdminMainApp_festivalmaste_festival_master_header_id__a65f92d6" ON public."AdminMainApp_festivalmasterchild" USING btree (festival_master_header_id_id);
 T   DROP INDEX public."AdminMainApp_festivalmaste_festival_master_header_id__a65f92d6";
       public            postgres    false    232                       1259    17124 6   AdminMainApp_gallerymaster_event_result_id_id_fcdab002    INDEX     �   CREATE INDEX "AdminMainApp_gallerymaster_event_result_id_id_fcdab002" ON public."AdminMainApp_gallerymaster" USING btree (event_result_id_id);
 L   DROP INDEX public."AdminMainApp_gallerymaster_event_result_id_id_fcdab002";
       public            postgres    false    256            �           1259    16940 >   AdminMainApp_organizingcom_committe_member_type_id_id_e28e81be    INDEX     �   CREATE INDEX "AdminMainApp_organizingcom_committe_member_type_id_id_e28e81be" ON public."AdminMainApp_organizingcommittemaster" USING btree (committe_member_type_id_id);
 T   DROP INDEX public."AdminMainApp_organizingcom_committe_member_type_id_id_e28e81be";
       public            postgres    false    230            �           1259    16941 ;   AdminMainApp_organizingcom_department_master_id_id_52fbbdc4    INDEX     �   CREATE INDEX "AdminMainApp_organizingcom_department_master_id_id_52fbbdc4" ON public."AdminMainApp_organizingcommittemaster" USING btree (department_master_id_id);
 Q   DROP INDEX public."AdminMainApp_organizingcom_department_master_id_id_52fbbdc4";
       public            postgres    false    230            �           1259    16942 >   AdminMainApp_organizingcom_festival_master_header_id__c41218c8    INDEX     �   CREATE INDEX "AdminMainApp_organizingcom_festival_master_header_id__c41218c8" ON public."AdminMainApp_organizingcommittemaster" USING btree (festival_master_header_id_id);
 T   DROP INDEX public."AdminMainApp_organizingcom_festival_master_header_id__c41218c8";
       public            postgres    false    230                       1259    17068 6   AdminMainApp_participantre_event_master_id_id_cc1bdf1a    INDEX     �   CREATE INDEX "AdminMainApp_participantre_event_master_id_id_cc1bdf1a" ON public."AdminMainApp_participantregistrationheader" USING btree (event_master_id_id);
 L   DROP INDEX public."AdminMainApp_participantre_event_master_id_id_cc1bdf1a";
       public            postgres    false    248                       1259    17085 >   AdminMainApp_participantre_participant_registration_h_77b9f09b    INDEX     �   CREATE INDEX "AdminMainApp_participantre_participant_registration_h_77b9f09b" ON public."AdminMainApp_participantregistrationchild" USING btree (participant_registration_header_id_id);
 T   DROP INDEX public."AdminMainApp_participantre_participant_registration_h_77b9f09b";
       public            postgres    false    252                       1259    17074 >   AdminMainApp_participantre_participant_registration_h_844dbde2    INDEX     �   CREATE INDEX "AdminMainApp_participantre_participant_registration_h_844dbde2" ON public."AdminMainApp_participantregistrationpayment" USING btree (participant_registration_header_id_id);
 T   DROP INDEX public."AdminMainApp_participantre_participant_registration_h_844dbde2";
       public            postgres    false    250                       1259    17086 :   AdminMainApp_participantre_participant_type_id_id_632439f0    INDEX     �   CREATE INDEX "AdminMainApp_participantre_participant_type_id_id_632439f0" ON public."AdminMainApp_participantregistrationchild" USING btree (participant_type_id_id);
 P   DROP INDEX public."AdminMainApp_participantre_participant_type_id_id_632439f0";
       public            postgres    false    252            �           1259    17207 6   AdminMainApp_sponsormaster_event_master_id_id_be06d640    INDEX     �   CREATE INDEX "AdminMainApp_sponsormaster_event_master_id_id_be06d640" ON public."AdminMainApp_sponsormaster" USING btree (event_master_id_id);
 L   DROP INDEX public."AdminMainApp_sponsormaster_event_master_id_id_be06d640";
       public            postgres    false    238            �           1259    17208 >   AdminMainApp_sponsormaster_festival_master_header_id__644f0d8b    INDEX     �   CREATE INDEX "AdminMainApp_sponsormaster_festival_master_header_id__644f0d8b" ON public."AdminMainApp_sponsormaster" USING btree (festival_master_header_id_id);
 T   DROP INDEX public."AdminMainApp_sponsormaster_festival_master_header_id__644f0d8b";
       public            postgres    false    238                       1259    17149 ;   AdminMainApp_usermaster_organizing_committe_master_a209b47a    INDEX     �   CREATE INDEX "AdminMainApp_usermaster_organizing_committe_master_a209b47a" ON public."AdminMainApp_usermaster" USING btree (organizing_committe_master_id_id);
 Q   DROP INDEX public."AdminMainApp_usermaster_organizing_committe_master_a209b47a";
       public            postgres    false    260                       1259    17150 0   AdminMainApp_usermaster_user_type_id_id_ba8b8ebd    INDEX     �   CREATE INDEX "AdminMainApp_usermaster_user_type_id_id_ba8b8ebd" ON public."AdminMainApp_usermaster" USING btree (user_type_id_id);
 F   DROP INDEX public."AdminMainApp_usermaster_user_type_id_id_ba8b8ebd";
       public            postgres    false    260            "           1259    17345    auth_group_name_a6ea08ec_like    INDEX     h   CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);
 1   DROP INDEX public.auth_group_name_a6ea08ec_like;
       public            postgres    false    266            '           1259    17285 (   auth_group_permissions_group_id_b120cbf9    INDEX     o   CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);
 <   DROP INDEX public.auth_group_permissions_group_id_b120cbf9;
       public            postgres    false    268            *           1259    17286 -   auth_group_permissions_permission_id_84c5c92e    INDEX     y   CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);
 A   DROP INDEX public.auth_group_permissions_permission_id_84c5c92e;
       public            postgres    false    268                       1259    17271 (   auth_permission_content_type_id_2f476e4b    INDEX     o   CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);
 <   DROP INDEX public.auth_permission_content_type_id_2f476e4b;
       public            postgres    false    264            2           1259    17301 "   auth_user_groups_group_id_97559544    INDEX     c   CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);
 6   DROP INDEX public.auth_user_groups_group_id_97559544;
       public            postgres    false    272            5           1259    17300 !   auth_user_groups_user_id_6a12ed8b    INDEX     a   CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);
 5   DROP INDEX public.auth_user_groups_user_id_6a12ed8b;
       public            postgres    false    272            8           1259    17315 1   auth_user_user_permissions_permission_id_1fbb5f2c    INDEX     �   CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);
 E   DROP INDEX public.auth_user_user_permissions_permission_id_1fbb5f2c;
       public            postgres    false    274            ;           1259    17314 +   auth_user_user_permissions_user_id_a95ead1b    INDEX     u   CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);
 ?   DROP INDEX public.auth_user_user_permissions_user_id_a95ead1b;
       public            postgres    false    274            /           1259    17340     auth_user_username_6821ab7c_like    INDEX     n   CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);
 4   DROP INDEX public.auth_user_username_6821ab7c_like;
       public            postgres    false    270            >           1259    17336 )   django_admin_log_content_type_id_c4bce8eb    INDEX     q   CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);
 =   DROP INDEX public.django_admin_log_content_type_id_c4bce8eb;
       public            postgres    false    276            A           1259    17337 !   django_admin_log_user_id_c564eba6    INDEX     a   CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);
 5   DROP INDEX public.django_admin_log_user_id_c564eba6;
       public            postgres    false    276            B           1259    17354 #   django_session_expire_date_a5c62663    INDEX     e   CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);
 7   DROP INDEX public.django_session_expire_date_a5c62663;
       public            postgres    false    277            E           1259    17353 (   django_session_session_key_c0390e0f_like    INDEX     ~   CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);
 <   DROP INDEX public.django_session_session_key_c0390e0f_like;
       public            postgres    false    277            J           2606    16993 X   AdminMainApp_eventmaster AdminMainApp_eventma_event_category_id_id_44ba300b_fk_AdminMain    FK CONSTRAINT       ALTER TABLE ONLY public."AdminMainApp_eventmaster"
    ADD CONSTRAINT "AdminMainApp_eventma_event_category_id_id_44ba300b_fk_AdminMain" FOREIGN KEY (event_category_id_id) REFERENCES public."AdminMainApp_eventcategorymaster"(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public."AdminMainApp_eventmaster" DROP CONSTRAINT "AdminMainApp_eventma_event_category_id_id_44ba300b_fk_AdminMain";
       public          postgres    false    4827    234    222            K           2606    16998 X   AdminMainApp_eventmaster AdminMainApp_eventma_festival_master_head_a341fcc1_fk_AdminMain    FK CONSTRAINT       ALTER TABLE ONLY public."AdminMainApp_eventmaster"
    ADD CONSTRAINT "AdminMainApp_eventma_festival_master_head_a341fcc1_fk_AdminMain" FOREIGN KEY (festival_master_header_id_id) REFERENCES public."AdminMainApp_festivalmasterheader"(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public."AdminMainApp_eventmaster" DROP CONSTRAINT "AdminMainApp_eventma_festival_master_head_a341fcc1_fk_AdminMain";
       public          postgres    false    4831    226    234            L           2606    17003 X   AdminMainApp_eventmaster AdminMainApp_eventma_participant_category_629bd6c4_fk_AdminMain    FK CONSTRAINT       ALTER TABLE ONLY public."AdminMainApp_eventmaster"
    ADD CONSTRAINT "AdminMainApp_eventma_participant_category_629bd6c4_fk_AdminMain" FOREIGN KEY (participant_category_id_id) REFERENCES public."AdminMainApp_participantcategorymaster"(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public."AdminMainApp_eventmaster" DROP CONSTRAINT "AdminMainApp_eventma_participant_category_629bd6c4_fk_AdminMain";
       public          postgres    false    224    234    4829            P           2606    17017 [   AdminMainApp_eventprizemaster AdminMainApp_eventpr_event_master_id_id_752a39f0_fk_AdminMain    FK CONSTRAINT     �   ALTER TABLE ONLY public."AdminMainApp_eventprizemaster"
    ADD CONSTRAINT "AdminMainApp_eventpr_event_master_id_id_752a39f0_fk_AdminMain" FOREIGN KEY (event_master_id_id) REFERENCES public."AdminMainApp_eventmaster"(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public."AdminMainApp_eventprizemaster" DROP CONSTRAINT "AdminMainApp_eventpr_event_master_id_id_752a39f0_fk_AdminMain";
       public          postgres    false    234    244    4846            Q           2606    17161 Y   AdminMainApp_eventprizemaster AdminMainApp_eventpr_prize_type_id_id_eb4004f8_fk_AdminMain    FK CONSTRAINT       ALTER TABLE ONLY public."AdminMainApp_eventprizemaster"
    ADD CONSTRAINT "AdminMainApp_eventpr_prize_type_id_id_eb4004f8_fk_AdminMain" FOREIGN KEY (prize_type_id_id) REFERENCES public."AdminMainApp_prizetypemastermodel"(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public."AdminMainApp_eventprizemaster" DROP CONSTRAINT "AdminMainApp_eventpr_prize_type_id_id_eb4004f8_fk_AdminMain";
       public          postgres    false    236    4848    244            R           2606    17151 ]   AdminMainApp_eventprizemaster AdminMainApp_eventpr_winner_position_id_i_79f6e072_fk_AdminMain    FK CONSTRAINT       ALTER TABLE ONLY public."AdminMainApp_eventprizemaster"
    ADD CONSTRAINT "AdminMainApp_eventpr_winner_position_id_i_79f6e072_fk_AdminMain" FOREIGN KEY (winner_position_id_id) REFERENCES public."AdminMainApp_winnerpositionmastermodel"(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public."AdminMainApp_eventprizemaster" DROP CONSTRAINT "AdminMainApp_eventpr_winner_position_id_i_79f6e072_fk_AdminMain";
       public          postgres    false    240    4854    244            W           2606    17101 V   AdminMainApp_eventresult AdminMainApp_eventre_event_master_id_id_8b3a227a_fk_AdminMain    FK CONSTRAINT     �   ALTER TABLE ONLY public."AdminMainApp_eventresult"
    ADD CONSTRAINT "AdminMainApp_eventre_event_master_id_id_8b3a227a_fk_AdminMain" FOREIGN KEY (event_master_id_id) REFERENCES public."AdminMainApp_eventmaster"(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public."AdminMainApp_eventresult" DROP CONSTRAINT "AdminMainApp_eventre_event_master_id_id_8b3a227a_fk_AdminMain";
       public          postgres    false    4846    254    234            X           2606    17106 X   AdminMainApp_eventresult AdminMainApp_eventre_participant_registra_d10b5911_fk_AdminMain    FK CONSTRAINT       ALTER TABLE ONLY public."AdminMainApp_eventresult"
    ADD CONSTRAINT "AdminMainApp_eventre_participant_registra_d10b5911_fk_AdminMain" FOREIGN KEY (participant_registration_header_id_id) REFERENCES public."AdminMainApp_participantregistrationheader"(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public."AdminMainApp_eventresult" DROP CONSTRAINT "AdminMainApp_eventre_participant_registra_d10b5911_fk_AdminMain";
       public          postgres    false    254    248    4867            Y           2606    17156 X   AdminMainApp_eventresult AdminMainApp_eventre_winner_position_id_i_6ee0ea91_fk_AdminMain    FK CONSTRAINT     
  ALTER TABLE ONLY public."AdminMainApp_eventresult"
    ADD CONSTRAINT "AdminMainApp_eventre_winner_position_id_i_6ee0ea91_fk_AdminMain" FOREIGN KEY (winner_position_id_id) REFERENCES public."AdminMainApp_winnerpositionmastermodel"(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public."AdminMainApp_eventresult" DROP CONSTRAINT "AdminMainApp_eventre_winner_position_id_i_6ee0ea91_fk_AdminMain";
       public          postgres    false    254    4854    240            O           2606    17011 Y   AdminMainApp_eventscheduler AdminMainApp_eventsc_event_master_id_id_6a1b8acd_fk_AdminMain    FK CONSTRAINT     �   ALTER TABLE ONLY public."AdminMainApp_eventscheduler"
    ADD CONSTRAINT "AdminMainApp_eventsc_event_master_id_id_6a1b8acd_fk_AdminMain" FOREIGN KEY (event_master_id_id) REFERENCES public."AdminMainApp_eventmaster"(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public."AdminMainApp_eventscheduler" DROP CONSTRAINT "AdminMainApp_eventsc_event_master_id_id_6a1b8acd_fk_AdminMain";
       public          postgres    false    234    4846    242            I           2606    16943 `   AdminMainApp_festivalmasterchild AdminMainApp_festiva_festival_master_head_a65f92d6_fk_AdminMain    FK CONSTRAINT       ALTER TABLE ONLY public."AdminMainApp_festivalmasterchild"
    ADD CONSTRAINT "AdminMainApp_festiva_festival_master_head_a65f92d6_fk_AdminMain" FOREIGN KEY (festival_master_header_id_id) REFERENCES public."AdminMainApp_festivalmasterheader"(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public."AdminMainApp_festivalmasterchild" DROP CONSTRAINT "AdminMainApp_festiva_festival_master_head_a65f92d6_fk_AdminMain";
       public          postgres    false    226    232    4831            Z           2606    17119 X   AdminMainApp_gallerymaster AdminMainApp_gallery_event_result_id_id_fcdab002_fk_AdminMain    FK CONSTRAINT     �   ALTER TABLE ONLY public."AdminMainApp_gallerymaster"
    ADD CONSTRAINT "AdminMainApp_gallery_event_result_id_id_fcdab002_fk_AdminMain" FOREIGN KEY (event_result_id_id) REFERENCES public."AdminMainApp_eventresult"(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public."AdminMainApp_gallerymaster" DROP CONSTRAINT "AdminMainApp_gallery_event_result_id_id_fcdab002_fk_AdminMain";
       public          postgres    false    256    254    4878            F           2606    16925 e   AdminMainApp_organizingcommittemaster AdminMainApp_organiz_committe_member_type_e28e81be_fk_AdminMain    FK CONSTRAINT       ALTER TABLE ONLY public."AdminMainApp_organizingcommittemaster"
    ADD CONSTRAINT "AdminMainApp_organiz_committe_member_type_e28e81be_fk_AdminMain" FOREIGN KEY (committe_member_type_id_id) REFERENCES public."AdminMainApp_committemembertypemaster"(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public."AdminMainApp_organizingcommittemaster" DROP CONSTRAINT "AdminMainApp_organiz_committe_member_type_e28e81be_fk_AdminMain";
       public          postgres    false    4833    230    228            G           2606    16930 e   AdminMainApp_organizingcommittemaster AdminMainApp_organiz_department_master_id_52fbbdc4_fk_AdminMain    FK CONSTRAINT       ALTER TABLE ONLY public."AdminMainApp_organizingcommittemaster"
    ADD CONSTRAINT "AdminMainApp_organiz_department_master_id_52fbbdc4_fk_AdminMain" FOREIGN KEY (department_master_id_id) REFERENCES public."AdminMainApp_departmentmaster"(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public."AdminMainApp_organizingcommittemaster" DROP CONSTRAINT "AdminMainApp_organiz_department_master_id_52fbbdc4_fk_AdminMain";
       public          postgres    false    4825    230    220            H           2606    16935 e   AdminMainApp_organizingcommittemaster AdminMainApp_organiz_festival_master_head_c41218c8_fk_AdminMain    FK CONSTRAINT       ALTER TABLE ONLY public."AdminMainApp_organizingcommittemaster"
    ADD CONSTRAINT "AdminMainApp_organiz_festival_master_head_c41218c8_fk_AdminMain" FOREIGN KEY (festival_master_header_id_id) REFERENCES public."AdminMainApp_festivalmasterheader"(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public."AdminMainApp_organizingcommittemaster" DROP CONSTRAINT "AdminMainApp_organiz_festival_master_head_c41218c8_fk_AdminMain";
       public          postgres    false    230    226    4831            S           2606    17063 h   AdminMainApp_participantregistrationheader AdminMainApp_partici_event_master_id_id_cc1bdf1a_fk_AdminMain    FK CONSTRAINT     	  ALTER TABLE ONLY public."AdminMainApp_participantregistrationheader"
    ADD CONSTRAINT "AdminMainApp_partici_event_master_id_id_cc1bdf1a_fk_AdminMain" FOREIGN KEY (event_master_id_id) REFERENCES public."AdminMainApp_eventmaster"(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public."AdminMainApp_participantregistrationheader" DROP CONSTRAINT "AdminMainApp_partici_event_master_id_id_cc1bdf1a_fk_AdminMain";
       public          postgres    false    234    248    4846            U           2606    17075 i   AdminMainApp_participantregistrationchild AdminMainApp_partici_participant_registra_77b9f09b_fk_AdminMain    FK CONSTRAINT     /  ALTER TABLE ONLY public."AdminMainApp_participantregistrationchild"
    ADD CONSTRAINT "AdminMainApp_partici_participant_registra_77b9f09b_fk_AdminMain" FOREIGN KEY (participant_registration_header_id_id) REFERENCES public."AdminMainApp_participantregistrationheader"(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public."AdminMainApp_participantregistrationchild" DROP CONSTRAINT "AdminMainApp_partici_participant_registra_77b9f09b_fk_AdminMain";
       public          postgres    false    248    4867    252            T           2606    17069 k   AdminMainApp_participantregistrationpayment AdminMainApp_partici_participant_registra_844dbde2_fk_AdminMain    FK CONSTRAINT     1  ALTER TABLE ONLY public."AdminMainApp_participantregistrationpayment"
    ADD CONSTRAINT "AdminMainApp_partici_participant_registra_844dbde2_fk_AdminMain" FOREIGN KEY (participant_registration_header_id_id) REFERENCES public."AdminMainApp_participantregistrationheader"(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public."AdminMainApp_participantregistrationpayment" DROP CONSTRAINT "AdminMainApp_partici_participant_registra_844dbde2_fk_AdminMain";
       public          postgres    false    4867    250    248            V           2606    17080 i   AdminMainApp_participantregistrationchild AdminMainApp_partici_participant_type_id__632439f0_fk_AdminMain    FK CONSTRAINT       ALTER TABLE ONLY public."AdminMainApp_participantregistrationchild"
    ADD CONSTRAINT "AdminMainApp_partici_participant_type_id__632439f0_fk_AdminMain" FOREIGN KEY (participant_type_id_id) REFERENCES public."AdminMainApp_participanttypemaster"(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public."AdminMainApp_participantregistrationchild" DROP CONSTRAINT "AdminMainApp_partici_participant_type_id__632439f0_fk_AdminMain";
       public          postgres    false    246    4864    252            M           2606    17197 X   AdminMainApp_sponsormaster AdminMainApp_sponsor_event_master_id_id_be06d640_fk_AdminMain    FK CONSTRAINT     �   ALTER TABLE ONLY public."AdminMainApp_sponsormaster"
    ADD CONSTRAINT "AdminMainApp_sponsor_event_master_id_id_be06d640_fk_AdminMain" FOREIGN KEY (event_master_id_id) REFERENCES public."AdminMainApp_eventmaster"(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public."AdminMainApp_sponsormaster" DROP CONSTRAINT "AdminMainApp_sponsor_event_master_id_id_be06d640_fk_AdminMain";
       public          postgres    false    234    238    4846            N           2606    17202 Z   AdminMainApp_sponsormaster AdminMainApp_sponsor_festival_master_head_644f0d8b_fk_AdminMain    FK CONSTRAINT       ALTER TABLE ONLY public."AdminMainApp_sponsormaster"
    ADD CONSTRAINT "AdminMainApp_sponsor_festival_master_head_644f0d8b_fk_AdminMain" FOREIGN KEY (festival_master_header_id_id) REFERENCES public."AdminMainApp_festivalmasterheader"(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public."AdminMainApp_sponsormaster" DROP CONSTRAINT "AdminMainApp_sponsor_festival_master_head_644f0d8b_fk_AdminMain";
       public          postgres    false    238    4831    226            [           2606    17166 W   AdminMainApp_usermaster AdminMainApp_usermas_organizing_committe__a209b47a_fk_AdminMain    FK CONSTRAINT       ALTER TABLE ONLY public."AdminMainApp_usermaster"
    ADD CONSTRAINT "AdminMainApp_usermas_organizing_committe__a209b47a_fk_AdminMain" FOREIGN KEY (organizing_committe_master_id_id) REFERENCES public."AdminMainApp_organizingcommittemaster"(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public."AdminMainApp_usermaster" DROP CONSTRAINT "AdminMainApp_usermas_organizing_committe__a209b47a_fk_AdminMain";
       public          postgres    false    230    260    4838            \           2606    17144 R   AdminMainApp_usermaster AdminMainApp_usermas_user_type_id_id_ba8b8ebd_fk_AdminMain    FK CONSTRAINT     �   ALTER TABLE ONLY public."AdminMainApp_usermaster"
    ADD CONSTRAINT "AdminMainApp_usermas_user_type_id_id_ba8b8ebd_fk_AdminMain" FOREIGN KEY (user_type_id_id) REFERENCES public."AdminMainApp_usertype"(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public."AdminMainApp_usermaster" DROP CONSTRAINT "AdminMainApp_usermas_user_type_id_id_ba8b8ebd_fk_AdminMain";
       public          postgres    false    4884    258    260            ^           2606    17280 O   auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;
 y   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm;
       public          postgres    false    4897    268    264            _           2606    17275 P   auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;
 z   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id;
       public          postgres    false    266    268    4902            ]           2606    17266 E   auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;
 o   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co;
       public          postgres    false    4892    264    262            `           2606    17295 D   auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;
 n   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id;
       public          postgres    false    4902    266    272            a           2606    17290 B   auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 l   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id;
       public          postgres    false    270    4910    272            b           2606    17309 S   auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;
 }   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm;
       public          postgres    false    274    4897    264            c           2606    17304 V   auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id;
       public          postgres    false    274    270    4910            d           2606    17326 G   django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co    FK CONSTRAINT     �   ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;
 q   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co;
       public          postgres    false    262    276    4892            e           2606    17331 B   django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 l   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id;
       public          postgres    false    270    4910    276               �   x�uͫ�0�a}�x��s�e��̐3+bн?�$%��_`�e=�	Bb;��C�5��J8�KJ0/�k��V3����I��m0��:\Z3e��k�,���X���G�'�=��`,ǒ�ҖY�wڐc�(p@�      �   o   x�m˫
�@ �|�+��p_Ϋ��֍�-���YN=׼��l��Z!U��$!	�<��X'A��c?a��ah?]�vp���$��}&
4�ߐ[5Z�1*g�h�1uq&�      �   �   x�mͻ�0@���
v�Ȏ�����D� ��<���"����N����i ِ�5m�,���ʹ�fk�����:�in�����$�c����^�|����'�I�C
����
*'�1��t�Ƙ7��6k           x�uнn� ���{e����ҡi�f�Bm D�ٴU߾`��%:L��9IJ	���8�M�(���������"R�
���Sd�.�h�͏͉v����}�/O��x�(Nb��q�p�
��]E��ope@�t��]p�|4��u��A�~>��*�Р4{$g���0�j3�C7������\�֯k� -a��U&v�|���\2]� ��'[��ol������/�j.&5��L����g��f[�=��WB�         b   x�m�1
�0й9����4)msO�Epq���c�����_��ED�`�:q1dAU���n�~����s л�o$O����TD+� �E�@Z ��,�         C   x�34�L�4202�50�54W04�24�25ֳ076���60�26�LL�����!cNcNC�=... ��A         �   x�u�;
A�zr��e��w�Cx�m��?�
;�#�H��C��uF��{����%zZ�%h)XN���V��x?�V��"�Өjk�2��C��4E���-m )�~��d��x�U"�G�	X���}B�Z���; ���-�I�         Z   x�3�4202�50�54�3�8K�&
�FV�V��z����V���)��y�1~ d�e��`�� #�Az&�FfX2����� �,�          |   x�3�LLJN�L�)/��J�LCb���!�f�%p������������������������gbJnfg�qqVgPfzF�^VA:n�%�i�q���o4�B��������1z\\\ ��.�            x������ � �      �      x������ � �         �   x����JA�s�Sx����M<z���Ȅɂ���qb��K����"�?�r�jA�6O��T�ø�l���i��:�Kg�H�������RGzG� 15*�Z��=GX?�����$a��1c���:�7IM��r�$��PT��%I�?��E��W-|�9�\!m&zg"�!Sa��5��`U/�R
S��D��(#���b�%���ػx;P��W#&k$\{�����k      �   U   x�3���K�I�,�4202�50�54Q04�"C=3sKCcmS+c�Ĕ��<�? �2�t/�/-���L��������=... �         %  x���[S�H ���W��eO��w�-/8�:XSEE��_�'f�t�ea��|9}.�@�k���hǕ���OӨ����y2�'q�ݣ([ă�.�Ái�������,g\08 �:`"`�J�7V�0F�)�`�����1N�ԝVf��׬5��1O�x*؀3ʥ�V�"�D�o �{�b��JP�%7v�%"�]�7_��@iʍ���"�DiL�Q�L�Hm��t1���w�"FC�0J�]E��&��(�
JDY��Sz��4�At�$eF��aJ��\�u�Ie��;��"ኼ3I�άW+�O�+�o����p�	�ͦ{�R���秧����,���Z)<��4�筪��}<;
�kLCX	�c��m�rO)�Q2�w;V�@BS%8c�ұ�ŋ_ݼ�j�\�?��am�J�_#���{˱�Ö�"�Y����^�g��Ð�AI���JΙ�~4�JrP�\��ԗ��l���fj$�yD����l���yM�F uN(Wx�<�Z��G`z�$���z9�L�,uX��x������u�Ȝ?�s�jL�z�Д��i��b�U��Q(�0Ij@\XG� !|�D@��q��*|��%��Ѹ�<|,*��_仢��1�����}�����K^�Wb�lU���`�k[<���8��V܍7���5�Y��:�%l�k��Ϗ'�>��uU`�^}���G8���prS���-�E��"�ּn�����!�Ut����#h�.q��%�I�H����0�qk�ZH�iM��89k]���%0]Z�!ɗ�c��·y�n�������I���Ѽa��S�,g�M�����4�&-b������	։��s���	�/,	N�pV�T��Pb���<�F�~#���(�>e��:�ɲ���<��Ƨ����!��Y6���Jc�*Px��xW��9�}(6/Ny�6xQ��pi�V�xB�֠/�G�p���Q�Z�{-���x8Zt�}�n����.cv�	<1�Ʒdu=���W�W�e���ӧ��7v<1�b H+�����;������\�           x�u�;oZA��˯�����Z�I��ts��dc����g���� Q b>fϞ9sq��炙s������e��W�AD5�7���~}z���b�Q+�`_1�X�Ӽ�w�C�D�e�JH�J�	�E���R�C1|�#@?���V���8ĳ ��������Z���t.W�B��XU�u����R~<<Bn_\�&HH	P���o/�����ū'�"!�$n=����� ����� 9 � ��AD����"T��1(*B�ՀSʜ�z��Бy-�1�XnW@̜��e:����m>4�w��1������S�0:=��}L*�t�dEU ��Z�i$~i�����:�քlZD ��i�7��%�\��Ш��-�;L/�	c�ŁQ0��)F<�R��"�(��.&5�3!��a��#���6)E��c��$c7&1\�pG���LA�>���0�a�8a��X���"F�K
�K)�)X�#uF����l#�����Xض7}s¼�z��,<L�	c��D�'�:�caä�9���Cqgat,ܦ�R��6�]�`[w��ڗ,hJ ",�01M��i7>�k^�U�D&�����珗�q{�����{\��9S���!Ko�E7;Y������+�u�D�bK?c� �ɬ#���k�Z"Si���z��+G�k����R̲}Z�i�9�M�fM(ɕ�r����?Q쌶."f�O�)m�o�?ۡ~��r�Ԟ�()x���8�~�諾���>Zk��3eף�C�^��@ZPr��(��������Z��$         �  x�}�=nA�zt
��	��9DN��@ ER��)�M�5 l��||;��������Jz�}P�A;������ۏ�����8����6h)-��<&��s�ZZ�5ӱ覃��v���xpŝ1�]z��1��Ž�/�g��
��Ʊc��ŵf<�Z�ʠ�t.��r��)���	��c���F��}�ǵ���=�'����}�ʞ+�$}7�Sz��裰A�����ϥ+�����b9���u���ߏ������sʏ{}T�3�}폳�ڸ}y쯺�v�k�7��S�n����XB�
M��ϵ���������g��;Q��V8��<�?�G��Aԕ���y�g���ޟA��ѩ?��e�K�uoAlE現o�k��ʏ���*M����W�Ͼ�O@eoܮ�����^��jN�i��n��?�VO�         q   x�mͱ
�0��9}��bI��<�q��K;\o�G���,�4��e�;��iD)yb#2ր���'�ek�?��+�7n�}�8J@�Yc��g�$��&	�)�t��s'̠,{      
   {   x�m��
1���S��-;�M�������Y�����AP�a��oЦ�gz��� `+�jZ%1�%������t<Ӵ�J���:?�88'u�.p��[t��4�a%�p_5�=ً��NBx�.+�         r   x�u�K
�0 ����K��E���.�t�H�X��ۋ[Ax��0�V�y����J{=q*��Bb=q�ֱ:G������(��˭.0�8w8�8=�?�"n�l�,��#�>��"r      "   �   x�m��
�0Dg�+���d˶��@� �i!�����)�nл;��o�����1q	#�l��J��5�(��k_n���͊�y~�H	*9r���a,�ŀ ��֎�Jĵ�=>�.�d_��q5H�
��
�~
����7          2   x�3�tL����,�2�t����,)IM�99ӸL8����=... v^         �   x�m�;�0E�z�
z�����;6@E�"\�$�W\P���+���,��u�ۉc6�}B�`����w�a��9������х̊�����n��4�0�`)�fp��Q)�*E�?����Z#	{�V��ι�7�      (      x������ � �      *      x������ � �      &   �  x��Xے�8|���l����Ʃ�bo��( sj��/ز%���M��F��q��ݏ��v;=��I������������~��]2�^B�Eo�!7�K,�{���X@Pe#����u��L��p!�ip�lC�cX�`[�!U���(������
P��g�ه� RИ���P@E��k�KV� �?�χ]x�T�� ��k@�φm�h���'_�q���i��eV�`�Xɋ��! ��h\�xq�0�
�a�*�[�U��+�{G�ia�kG�ga�[G���B�K�u�׶/�����oTpdC��}�A"Dಓ�B.9A��-�Ór�s�l��-�UI�:p.� �h���d�*Ą}&9n!�J�g�)����o�>-?�ة՞�2TvJclH4(�NqL �
�S����dt��&�u�����ʹ��0�x#e�=��䍚q��ZI�卖�q%t���~D���O_�����]����YS\ ��`�׀��5���T)���t��s��H����N?<ږS@'��8 ��5o+I%�fbb�9I1ۃbb-mHI)hP1!t�i����g�Dd�ԁ��U*�i!�S\�9kZ��"^�VRU��\����5<nYQ��ʫ2u�,=x�@�J�(�<P�P�ϓ�������U�sL�Z�� ��C��ނ�S�P��^�p�!Lf�y�i�h��������c�	�����̼�Itj�(zz��y��K�^����k��y]�o�q�� ���F_	���[a$|1��9����d�I��Cs��r�43�-��\.M�q�������6v�ѝ;�n�{$$����0I���
U!.��p'���y�m�՜�]x�EA�o�3]DүRH5:�ET��T�Ȍ�t�R,�Ws���"2Q��	��Փ��ju/U��Kju�jJTSE������)D���w��G���z�f�Q5�f����~PI���#������_�}]/�]��M��>������7�Ѷ��?�Ne��zȃU�����0�q����'��9N"��S�'���i��JT��N]Wu�B���i(�E%wz���L܎!���
�I��QB2�Yx�"��j�/Zēx-�t"F���b�#~㸃�i�5��9�Ȅ�4�@4Bv%��� ͔�wzP���wj�L)-�=<�����Om�� |~ݝ�0&Va�P1�V!����FR��W�������      ,      x������ � �      .      x������ � �      0      x������ � �      2      x������ � �      $   =  x���Mr� ��p�NM��9@o��U��F�t��b;	������'�'UL6-�N���s�d[�������G��<_�. ����){����,�5��c�|ӗD{���c�dd��ܾ44�%E�*����ᜤZFP���R}��\k���Y��H�9K=�-�&�Di��1#0�@�ѩڪ4:R����EF���k�uë�B�S~[j�'Ď&u��uM���_�=�����K|͊א	�H2Oud(���^�y�\���)�Zh� t:��VR'��Ōq������0eft�Z �ޗظ43�W�w�����9�ļC�      �   @  x����r�6�����}g=$x������02�p*�*%��}�R�vH��MbK��@x�}���{�oBX�ΎV7@@�!��W�v��!�2�8����WAyӺO�ޜ�S����ڛƌ�˷�e���ӕN���Y�.��0��ck����h�2��s�Gsp��^��^�Λ�	)��&Xf��w3��S7����EG#��xF��vmk�Ѵ�}3~<�fu�����O��O��Ӫ�9��cK(VP��Osaq�]78��A	��Վ��p5e�ֶ��x��Ue(q���`���Ѻn	�}7%`�b1��r��7ñ�A7��R�q�y��W��$q�p�Ta��$�J�(��ӭQۮ3�w��z�M�b��ʶƩ�q&7�������(�*Ǚ&1(�L�sP.�;I@���lDH�d��d5R�fh(��x��U�mH��Ϥ�il{��*e�?'f�%o��`�T�LC��L��_�~�<���b�����X+	���st����3W�ʭ��t뎁~G�d��f�@q���g���0{H2��P������u�\�A��k����*F��'@�X�[�^��ɪ���=�-T\�7�L�@
�s�2q-���>N.>����2��1Ʉ	�������
UdK�7����L� ���%8��ޯE��iQC��u�YF��hS#[�8�X<�7�v�ĩ��G#�����1-{!�c�w���)j3��ޗ�F)�<Ɠ�3��9��ܐC�ot�`��!"�y,aZ���n�P*Dl?����ۇ�j�arl�ͭ���¯���0H		G.��Rz��$�^��?�[���b��4%�Jv�iB�N���!�M��@%���h}
��5���*x�KX��=�����0��>���f��F=\!e1R�^ӈ��@I�UY���1��H���хv�����%V�>�kZ5ݏ�E�ވ��ʝ�r��'ջ��>�Nl��~�\8�p6����B^����ͧ�[���0�1��2M�<Uܲ���It�7�+�;$wT��Ӓȳ1A����O��R��E�X�ޡ*�0�����ؾ������      3   �   x���ʂ0  ��|��#�!k�ΰ��H�O�@L��l��Ӟ���Zp��|j�Լz�%z|�Z�VW?K�0�`VW��
���_��w��g�+͢K�c�^���03�cǹR��ߜ+��ΡP��ĥ��fI*p�E\�D8������&��TE~�b����Y��p	m�ŶiBvp,��q7���=�     